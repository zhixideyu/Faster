from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'rss/(?P<xml_name>\w+)', rss, name='rss'),
    url(r'^feed/', feed, name='feed'),
]