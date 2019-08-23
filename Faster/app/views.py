from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.core.cache import cache
from .models import Article
from basics.models import RssSubscription
# Create your views here.


class InfoListView(ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'

    def get_queryset_cache_key(self):
        return NotImplementedError

    def get_queryset_data(self):
        return NotImplementedError

    def get_queryset_from_cache(self, cache_key):
        """
        缓存页面数据
        :param cache_key:
        :return:
        """
        value = cache.get(cache_key)
        if value:
            return value
        else:
            article_list = self.get_queryset_data()
            return article_list

    def get_queryset(self):
        key = self.get_queryset_cache_key()
        return self.get_queryset_from_cache(key)


class IndexView(InfoListView):
    """ 首页 """

    def get_queryset_data(self):
        article_list = Article.objects.filter(status='p')
        return article_list

    def get_queryset_cache_key(self):
        cache_key = 'index'
        return cache_key

    def get_context_data(self, **kwargs):
        kwargs['index'] = True
        return super(IndexView, self).get_context_data(**kwargs)


class ComprehensiveView(ListView):
    context_object_name = 'article_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        kwargs['gather'] = True
        return super(ComprehensiveView, self).get_context_data(**kwargs)


class ScienceView(ListView):
    template_name = 'tools.html'

    def get_context_data(self, **kwargs):
        kwargs['science'] = True
        return super(ScienceView, self).get_context_data(**kwargs)


class RecreationView(ListView):

    context_object_name = 'article_list'
    template_name = 'forum_main.html'

    def get_queryset(self):
        return

    def get_context_data(self, **kwargs):
        kwargs['recreation'] = True
        return super(RecreationView, self).get_context_data(**kwargs)


class PythonView(ListView):
    pass



