import re
import markdown

from app.models import Article
from django.views.generic import DetailView
from django.shortcuts import render, render_to_response

# Create your views here.


class ArticleDetailView(DetailView):
    """ 文章详情 """

    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article_info'
    # 定义用来获取对应的单挑数据，需要传递主键的值
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        """ 获取pk_url_kwarg中所要查找的对象类似ListView的get_queryset """
        obj = super(ArticleDetailView, self).get_object()
        obj.content = markdown.markdown(
            re.sub(re.compile('<.*?>'), '', obj.content),
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                # 允许生成目录
                'markdown.extensions.toc',
            ]
        )
        if self.request.user != obj.author:
            obj.viewed()
        return obj





