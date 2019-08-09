import markdown
import json

from django.shortcuts import render, render_to_response
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.views import View
from app.models import Article


# Create your views here.


def detail_api(request):
    article_id = request.GET.get('article_id', 1)
    article_info = Article.objects.get(id=article_id).to_dict()
    return HttpResponse(
        json.dumps(article_info, ensure_ascii=False),
        content_type="application/json,charset=utf-8")

