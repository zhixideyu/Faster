import time
import datetime
import PyRSS2Gen
from Faster.settings import *


class Feed(object):
    """ 将数据生成xml格式 """

    def __init__(self, target_title, target_link, info, description=None, xml_name=None):
        self.target_title = target_title
        self.target_link = target_link
        self.target_description = description
        self.target_info = info
        self.xml_name = xml_name

    def create(self):
        items = list()
        for info in self.target_info:
            items.append(PyRSS2Gen.RSSItem(
                title=info[1],
                link=self.target_link.split('.com')[0] + '.com' + '/' + info[0].strip('/') + '/' if 'http' not in info[0] else info[0],
                description=info[2] if len(info) == 3 else '快捷社区：专注于发现和分享！'
            ),)
        rss = PyRSS2Gen.RSS2(
            title=self.target_title,
            link=self.target_link,
            description=self.target_description,
            lastBuildDate=datetime.datetime.now(),
            items=items)
        if self.xml_name:
            filename = '{}'.format(self.xml_name)
            rss.write_xml(open(BASE_DIR + '/feed/templates/xml_html/{}'.format(filename), 'w', encoding='utf-8'), encoding='utf-8')
        else:
            filename = '{}.xml'.format(str(int(time.time())))
            rss.write_xml(open(BASE_DIR + '/feed/templates/xml_html/{}'.format(filename), "w", encoding='utf-8'), encoding='utf-8')
            return filename


