# -*- coding:utf-8 -*-
import re
import json
import requests
import jmespath
from lxml import etree
from .models import RssInfoSpider, RssResultInfo


class RssSpider(object):
    """ RSS爬虫 """

    def __init__(self, xml_name, limit, next_href_rule, url):
        self.xml_name = xml_name
        self.limit = int(limit)
        self.infos_list = list()
        self.base_url = url
        self.next_href_rule = next_href_rule
        self.rss_info = RssInfoSpider.objects.get(xml_name=self.xml_name)

    def parse_html(self, url, body_status=False):
        """ 获取页面源码 """
        response = requests.get(url)

        if self.rss_info.encode:
            response.encoding = '{}'.format(self.rss_info.encode)

        html = response.text

        if body_status:
            root = etree.HTML(html.encode(response.encoding).decode('utf-8'))
            return root

        return self.parse_home_page(html)

    def parse_home_page(self, html):
        """ 首页 """
        title = re.findall(re.compile('{}'.format(self.rss_info.feed_title_rule), re.S), html)[0]
        infos = re.findall(re.compile('{}'.format(self.rss_info.connect_rule), re.S), html)

        for info in infos:
            if self.base_url:
                body_info = self.parse_body(info[0])
                info = (info[0], info[1], ''.join(body_info))
            self.infos_list.append(info)

        if len(self.infos_list) < self.limit:
            self.parse_next_page(html)
        return title, self.infos_list

    def parse_body(self, url):
        """ 文章主体 """
        if 'http' not in url:
            url = self.base_url.split('.com')[0] + '.com' + '/' + url.strip('/') + '/'

        root = self.parse_html(url, body_status=True)
        body_info = root.xpath('//p//text()')
        return body_info

    def parse_next_page(self, html):
        """ 下一页 """
        root = etree.HTML(html)
        next_url = root.xpath('//a[text()="下一页"]/@href')
        if len(next_url) == 0:
            if self.next_href_rule:
                next_url = re.findall(re.compile('{}'.format(self.next_href_rule), re.S), html)[0]
            else:
                return
        else:
            next_url = next_url[0]

        if 'http' not in next_url:
            next_url = self.base_url.split('.com')[0] + '.com' + '/' + next_url.strip('/') + '/'

        self.parse_html(next_url)


def process_data(request, rss_info, xml_name, feed_title):
    """ 筛选数据 """
    filter_title = request.GET.get('filter_title')
    filterout_title = request.GET.get('filterout_title')
    rss_rule_info = RssInfoSpider.objects.get(xml_name=xml_name)
    for info in rss_info:
        RssResultInfo(
            xml_name_id=rss_rule_info.id, url=info[0], title=info[1],
            feed_titile=feed_title, feed_url=rss_rule_info.url
            ).save()
    if filterout_title:
        rss_info = RssResultInfo.objects.exclude(title__icontains=filterout_title).values().all()
    elif filter_title:
        rss_info = RssResultInfo.objects.filter(title__icontains=filter_title).all().values()
    else:
        rss_info = RssResultInfo.objects.all().values()
    return [(info['url'], info['title']) for info in rss_info]


def start_rss_spider():
    """ 从数据库中运行任务 """
    spider_info = RssInfoSpider.objects.all().values()
    for info in spider_info:
        title_rule = info['feed_title_rule']
        connect_rule = info['connect_rule']
        encode = info['encode']
        url = info['url']
        xml_name_id = info['id']
        response = requests.get(url)
        if encode:
            response.encoding = '{}'.format(encode)
        target_title = re.findall(re.compile('{}'.format(title_rule), re.S), response.text)[0]
        infos = re.findall(re.compile('{}'.format(connect_rule), re.S), response.text)
        for info in infos:
            RssResultInfo(title=info[1], url=info[0], description=info[2], xml_name_id=xml_name_id, feed_titile=target_title, feed_url=url).save()


class JMESPathExtractor(object):
    """
    用JMESPath实现的抽取器，对于json格式数据实现简单方式的抽取。
    """
    def extract(self, query=None, body=None):
        try:
            return jmespath.search(query, json.loads(body))
        except Exception as e:
            raise ValueError("Invalid query: " + query + " : " + str(e))