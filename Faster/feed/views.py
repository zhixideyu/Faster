import re
import json
import requests
import operator

from .feeds import Feed
from django.http import JsonResponse
from json.decoder import JSONDecodeError
from django.views.generic import View
from .cron import RssSpider, process_data, JMESPathExtractor
from .models import RssInfoSpider, RssResultInfo
from django.shortcuts import render, render_to_response


# Create your views here.


class FeedView(View):
    def get(self, request):
        return render(request, 'tools.html')

    def post(self, request):
        reload_button = request.POST.get('reload')
        extract_button = request.POST.get('extract')
        create_button = request.POST.get('create')
        target_url = request.POST.get('target_url')
        json_extract_button = request.POST.get('json_extract')
        json_create_button = request.POST.get('json_create')
        if reload_button:
            return reload_detection(request, target_url)
        elif extract_button:
            return extract_detection(request)
        elif create_button or json_create_button:
            return create_detection(request, target_url)
        elif json_extract_button:
            return json_extract_detection(request)


def reload_detection(request, target_url):
    """ 加载 """
    encode = request.POST.get('encode')
    response = requests.get(target_url)
    if response.status_code == 200:
        if encode:
            response.encoding = '{}'.format(encode)
        result = {
            'reload_status': 1,
            'msg': response.text,
        }
        return JsonResponse(result)
    else:
        result = {
            'reload_status': 0,
            'msg': '发生错误，状态码：{}'.format(response.status_code)
        }
        return JsonResponse(result)


def extract_detection(request):
    """ 提取 """
    html = request.POST.get('html')
    pattern = request.POST.get('pattern')
    if len(pattern.split('(.*?)')) - 1 < 2:
        result = {
            'extract_status': 0,
            'msg': '该表达式不符合要求，请仔细阅读RSS须知！'
        }
        return JsonResponse(result)
    infos = re.findall(re.compile('{}'.format(pattern), re.S), html)
    infos = [str(info) + '\n' for info in infos]
    title_rule = '<title>(.*?)</title>'
    target_title = re.findall(re.compile('{}'.format(title_rule), re.S), html)
    result = {
        'extract_status': 1,
        'infos': infos,
        'title': target_title,
    }
    return JsonResponse(result)


def create_detection(request, target_url):
    """ 创建 """
    title = request.POST.get('title_name')
    link = request.POST.get('link')
    pattern = request.POST.get('pattern')
    html = request.POST.get('html')
    encode = request.POST.get('encode')
    next_page_rule = request.POST.get('next_page')
    feed_description = request.POST.get('description', title)

    json_url = request.POST.get('json_url')
    json_title = request.POST.get('json_title')
    json_description = request.POST.get('json_description')
    json_link = request.POST.get('json_link')
    json_feed_link = request.POST.get('json_feed_link')
    json_feed_title = request.POST.get('json_feed_title')
    json_feed_description = request.POST.get('json_feed_description')

    if json_url:
        target_url = json_url
        if json_description:
            pattern = [json_title, json_description, json_link]
        else:
            pattern = [json_title, json_link]

    rss_info = RssInfoSpider.objects.filter(url=target_url, connect_rule=pattern)
    if len(rss_info) == 0:
        if json_url:
            body = requests.get(json_url)
            J = JMESPathExtractor()
            r = '(?<=\\[)[^\\]]+'
            infos = list()
            for x in range(0, 20):
                title = J.extract(query=re.sub(r, str(x), json_title), body=body.text)
                if json_description:
                    description = J.extract(query=re.sub(r, str(x), json_description), body=body.text)
                else:
                    description = '未选择数据'
                link = J.extract(query=re.sub(r, str(x), json_link), body=body.text)
                infos.append((link, title, description))
                if title == '' and link == '':
                    break
            link = json_feed_link
            title = json_feed_title
            feed_description = json_feed_description
        else:
            infos = re.findall(re.compile('{}'.format(pattern), re.S), html)
        xml_name = Feed(
            target_link=link, target_title=title, info=infos,
            description=feed_description).create()

        if json_url:
            RssInfoSpider(
                url=target_url, connect_rule=pattern,
                xml_name=xml_name, next_href_rule=next_page_rule, encode=encode, type='json', feed_title_rule=title).save()
        else:
            RssInfoSpider(
                url=target_url, connect_rule=pattern, xml_name=xml_name, next_href_rule=next_page_rule,
                encode=encode).save()

        if json_url:
            result = {
                'json_extract_status': 1,
                'url': 'http://47.93.186.125:9702/science/rss?xml_name={}'.format(xml_name)
            }
        else:
            result = {
                'create_status': 1,
                'url': 'http://47.93.186.125:9702/science/rss?xml_name={}'.format(xml_name)
            }
        return JsonResponse(result)
    else:
        if json_url:
            result = {
                'json_extract_status': 0,
                'msg': '该源已存在，请勿重复提交！\nhttp://47.93.186.125:9702/science/rss?xml_name={}'.format(
                    rss_info[0].xml_name)
            }
        else:
            result = {
                'create_status': 0,
                'msg': '该源已存在，请勿重复提交！\nhttp://47.93.186.125:9702/science/rss?xml_name={}'.format(
                    rss_info[0].xml_name)
            }
        return JsonResponse(result)


def json_extract_detection(request):
    json_url = request.POST.get('json_url')
    json_title = request.POST.get('json_title')
    json_description = request.POST.get('json_description')
    json_link = request.POST.get('json_link')
    body = requests.get(json_url)
    try:
        J = JMESPathExtractor()
        title = J.extract(query=json_title, body=body.text)
        if json_description:
            description = J.extract(query=json_description, body=body.text)
        else:
            description = '未选择数据'
        link = J.extract(query=json_link, body=body.text)
    except Exception as e:
        result = {
            'json_extract_status': 0,
            'msg': '发生错误!'
        }
    else:
        result = {
            'json_extract_status': 1,
            'infos': '1：' + title + '\n' + '2：' + description + '\n' + '3：' + link
        }
    return JsonResponse(result)


def rss(request):
    """ RSS源 """
    xml_name = request.GET.get('xml_name')
    limit = request.GET.get('limit', 20)
    mode = request.GET.get('mode')
    rss = RssInfoSpider.objects.get(xml_name=xml_name)
    xml_name_id = rss.id
    url = rss.url
    if rss.type == 'json':
        r = '(?<=\\[)[^\\]]+'
        J = JMESPathExtractor()
        pattern = rss.connect_rule
        body = requests.get(rss.url)
        feed_title = rss.feed_title_rule
        if len(eval(pattern)) == 3:
            json_title = eval(pattern)[0]
            json_description = eval(pattern)[1]
            json_link = eval(pattern)[2]
        else:
            json_title = eval(pattern)[0]
            json_description = None
            json_link = eval(pattern)[1]
        rss_info = list()
        for x in range(0, 20):
            title = J.extract(query=re.sub(r, str(x), json_title), body=body.text)
            link = J.extract(query=re.sub(r, str(x), json_link), body=body.text)
            if json_description:
                description = J.extract(query=re.sub(r, str(x), json_description), body=body.text)
                rss_info.append((link, title, description))
            else:
                rss_info.append((link, title))
            if title == '' and link == '':
                break
    else:
        next_href_rule = rss.next_href_rule
        if mode == 'fulltext':
            get_body = rss.url
        else:
            get_body = False
        feed_title, rss_info = RssSpider(
            xml_name=xml_name, limit=limit, next_href_rule=next_href_rule, url=get_body).parse_html(url)
    process_rss_info = process_data(request, rss_info, xml_name, feed_title)
    Feed(target_link=url, target_title=feed_title, info=process_rss_info[:int(limit)], xml_name=xml_name).create()
    RssResultInfo.objects.filter(xml_name_id=xml_name_id).delete()
    return render_to_response('xml_html/{}'.format(xml_name), content_type="text/xml")
