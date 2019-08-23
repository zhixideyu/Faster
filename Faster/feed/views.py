import re
import requests
import operator

from .feeds import Feed
from .cron import RssSpider, process_data
from functools import reduce
from django.db.models import Q
from django.http import JsonResponse
from .models import RssInfoSpider, RssResultInfo
from django.shortcuts import render, render_to_response
# Create your views here.


def feed(request):
    """ 自定义RSS源 """
    if request.method == 'GET':
        feed = True
        return render(request, 'tools.html', {'feed': feed})
    elif request.method == 'POST':
        target_url = request.POST.get('target_url')
        encode = request.POST.get('encode')
        pattern = request.POST.get('pattern')
        title = request.POST.get('title_name')
        link = request.POST.get('link')
        next_page_rule = request.POST.get('next_page')
        description = request.POST.get('description', '快捷社区：专注于发现和分享！')
        create = request.POST.get('create')
        try:
            if target_url:
                if re.match(r'^https?:/{2}\w.+$', target_url):
                    response = requests.get(target_url)
                    if response.status_code == 200:
                        if encode:
                            response.encoding = '{}'.format(encode)
                        if pattern:
                            infos = re.findall(re.compile('{}'.format(pattern), re.S), response.text)
                            title_rule = '<title>(.*?)</title>'
                            target_title = re.findall(re.compile('{}'.format(title_rule), re.S), response.text)
                            if create == 'create':
                                if RssInfoSpider.objects.get(url=target_url, connect_rule=pattern):
                                    result = {
                                        'status': 0,
                                        'msg': '请勿重复提交！'
                                    }
                                    return JsonResponse(result)
                                else:
                                    xml_name = Feed(target_link=link, target_title=title, info=infos, description=description).create()
                                    RssInfoSpider(url=target_url, feed_title_rule=title_rule, connect_rule=pattern, xml_name=xml_name, next_href_rule=next_page_rule).save()
                                    result = {
                                        'status': 1,
                                        'url': 'http://47.93.186.125:9702/science/rss?xml_name={}'.format(xml_name)
                                    }
                                    return JsonResponse(result)
                            else:
                                result = {
                                    'status': 1,
                                    'infos': infos,
                                    'title': target_title,
                                    'link': target_url
                                }
                                return JsonResponse(result)
                        result = {
                            'status': 1,
                            'msg': response.text,
                        }
                        return JsonResponse(result)
                    else:
                        result = {
                            'status': 0,
                            'msg': '发生错误，状态码：{}'.format(response.status_code)
                        }
                        return JsonResponse(result)
                else:
                    result = {
                        'status': 0,
                        'msg': 'URL格式错误!'
                    }
                    return JsonResponse(result)
            else:
                result = {
                    'status': 0,
                    'msg': '请全部填写后在提交!'
                }
                return JsonResponse(result)
        except Exception as e:
            result = {
                'status': 0,
                'msg': e
            }
            return JsonResponse(result)


def rss(request):
    """ RSS源 """
    xml_name = request.GET.get('xml_name')
    limit = request.GET.get('limit', 20)
    mode = request.GET.get('mode')
    rss_info = RssInfoSpider.objects.get(xml_name=xml_name)
    next_href_rule = rss_info.next_href_rule
    url = rss_info.url
    if mode == 'fulltext':
        get_body = rss_info.url
    else:
        get_body = False
    xml_name_id = rss_info.id
    feed_title, rss_info = RssSpider(
        xml_name=xml_name, limit=limit, next_href_rule=next_href_rule, url=get_body).parse_html(url)
    process_rss_info = process_data(request, rss_info, xml_name, feed_title)
    Feed(target_link=url, target_title=feed_title, info=process_rss_info[:int(limit)], xml_name=xml_name).create()
    RssResultInfo.objects.filter(xml_name_id=xml_name_id).delete()
    return render_to_response('xml_html/{}'.format(xml_name), content_type="text/xml")







