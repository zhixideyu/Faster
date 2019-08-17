import time
import datetime
import PyRSS2Gen
from Faster.settings import *


class Feed(object):

    def __init__(self, target_title, target_link, info, description=None):
        self.target_title = target_title
        self.target_link = target_link
        self.target_description = description
        self.target_info = info

    def create(self):
        items = list()
        for info in self.target_info:
            items.append(PyRSS2Gen.RSSItem(
                title=info[1],
                link=info[0]))
        rss = PyRSS2Gen.RSS2(
            title=self.target_title,
            link=self.target_link,
            description="快捷社区：专注于发现和分享！",
            lastBuildDate=datetime.datetime.now(),
            items=items)
        filename = '{}.xml'.format(str(int(time.time())))
        rss.write_xml(open(BASE_DIR + '/feed/templates/xml_html/{}'.format(filename), "w", encoding='utf-8'), encoding='utf-8')
        return filename