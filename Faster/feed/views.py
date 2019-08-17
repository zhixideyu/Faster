import re
import requests
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
from .feeds import Feed
# Create your views here.


def feed(request):
    if request.method == 'GET':
        return render(request, 'tools.html')
    elif request.method == 'POST':
        target_url = request.POST.get('target_url')
        encode = request.POST.get('encode')
        pattern = request.POST.get('pattern')
        title = request.POST.get('title_name')
        link = request.POST.get('link')
        description = request.POST.get('description', '快捷社区：专注于发现和分享！')
        if target_url:
            if re.match(r'^https?:/{2}\w.+$', target_url):
                response = requests.get(target_url)
                if encode:
                    response.encoding = '{}'.format(encode)
                if pattern:
                    infos = re.findall(re.compile('{}'.format(pattern), re.S), response.text)
                    rule = '<title>(.*?)</title>'
                    target_title = re.findall(re.compile('{}'.format(rule), re.S), response.text)
                    if title != 'undefined' and link != 'undefined':
                        xml_name = Feed(target_link=link, target_title=title, info=infos, description=description).create()
                        result = {
                            'status': 2,
                            'url': 'http://47.93.186.125:9702/science/rss/{}'.format(xml_name)
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
                    'msg': 'URL格式错误!'
                }
                return JsonResponse(result)
        else:
            result = {
                'status': 0,
                'msg': '请全部填写后在提交!'
            }
            return JsonResponse(result)


def rss(request, xml_name):
    """ 返回xml """
    return render_to_response('xml_html/{}.xml'.format(xml_name))





