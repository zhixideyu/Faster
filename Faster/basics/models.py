from django.db import models
from datetime import datetime
from django.urls import reverse


# Create your models here.


class RssSubscription(models.Model):
    STATUS_CHOICES = (
        ('d', '测试'),
        ('p', '发布'),
        ('s', '私有'),
    )

    href = models.CharField(max_length=225, verbose_name='RSS地址')
    title = models.CharField(max_length=50, verbose_name='RSS描述')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p', verbose_name='RSS状态')

    class Meta:
        db_table = 'rss_subscription'
        verbose_name = 'RSS订阅'
        verbose_name_plural = verbose_name


class WeiBoHot(models.Model):
    """ 微博热榜 """

    key_word = models.CharField(max_length=225, verbose_name='关键词')
    href = models.CharField(max_length=225, verbose_name='地址')
    grade = models.CharField(max_length=225, verbose_name='等级', default='无')
    date = models.DateTimeField(max_length=255, verbose_name='日期', default=datetime.now)

    class Meta:
        db_table = 'weibo_hot'
        verbose_name = '微博热榜'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):

        return self.href


class BaiDuHot(models.Model):
    """ 百度热榜 """

    key_word = models.CharField(max_length=225, verbose_name='关键词')
    href = models.CharField(max_length=225, verbose_name='地址')
    date = models.DateTimeField(max_length=225, verbose_name='日期', default=datetime.now)

    class Meta:
        db_table = 'baidu_hot'
        verbose_name = '百度热榜'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):

        return self.href
