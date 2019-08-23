from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'rss/', rss, name='rss'),
    url(r'^feed/', feed, name='feed'),
]