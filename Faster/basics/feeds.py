from .models import BaiDuHot, WeiBoHot
from app.feeds import AllArticleRssFeed


class BaiDuHotRssFeed(AllArticleRssFeed):
    link = 'http://47.93.186.125:9702/feed_baidu_hot'

    def items(self):
        return BaiDuHot.objects.all().order_by('-date')

    def item_title(self, item):
        return item.key_word

    def item_description(self, item):
        return None

    def item_pubdate(self, item):
        return item.date


class WeiBoHotRssFed(BaiDuHotRssFeed):
    link = 'http://47.93.186.125:9702/feed_weibo_hot'

    def items(self):
        return WeiBoHot.objects.all().order_by('-date')
