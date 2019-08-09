from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from .models import Article
from basics.views import detail_api
# Create your views here.


class IndexView(ListView):
    context_object_name = 'article_list'
    template_name = 'index.html'

    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset


class ComprehensiveView(ListView):
    context_object_name = 'article_list'
    template_name = 'search_results.html'

    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset



class ScienceView(ListView):
    pass


class RecreationView(ListView):

    context_object_name = 'article_list'
    template_name = 'forum_main.html'

    def get_queryset(self):
        return


class PythonView(ListView):
    pass


class DetailView(View):

    def get(self, request):
        return render(request, 'article.html')
