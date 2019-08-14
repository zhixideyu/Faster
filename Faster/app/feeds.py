from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed
from django.shortcuts import reverse
from .models import Article
from Faster.utils import CommonMarkdown


class AllArticleRssFeed(Feed):
    feed_type = Rss201rev2Feed

    # 显示在聚合阅读器上的标题
    title = '快捷社区'

    # 通过聚合阅读器跳转到网站的地址
    link = 'http://47.93.186.125:9702/feed'

    # 显示在聚合阅读器上的描述信息
    description = '快捷社区：专注于发现和分享'

    # 显示的内容条目
    def items(self):
        return Article.objects.all()

    # 内容条目的标题
    def item_title(self, item):
        tags = [str(x).split(': ')[-1].replace('>', '') for x in item.article_tags.all()]
        if len(tags) <= 2:
            pass
        else:
            tags = tags[:2]
        return '[%s] %s' % (','.join(tags), item.title)

    # 内容描述
    def item_description(self, item):
        return item.content

    def item_pubdate(self, item):
        return item.publish_time

    # # 文章详情路由
    # def item_link(self, item):
    #     return reverse('detail', kwargs={
    #         'article_id': item.id
    #     })



