from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^detail/(?P<article_id>\w+)', ArticleDetailView.as_view(), name='detail'),
]