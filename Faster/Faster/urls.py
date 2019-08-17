"""Faster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from app.feeds import AllArticleRssFeed
from basics.feeds import BaiDuHotRssFeed, WeiBoHotRssFed
from django.contrib import admin
from django.views.static import serve
from . import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^user/', include('user.url')),
    url(r'^article/', include('basics.url')),
    url(r'^feed_baidu_hot/$', BaiDuHotRssFeed(), name='baidu_hot'),
    url(r'^feed_weibo_hot/$', WeiBoHotRssFed(), name='weibo_hot'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^science/', include('feed.url')),
    url(r'^', include('app.url')),
]
