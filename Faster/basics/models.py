from django.db import models
from datetime import datetime


# Create your models here.
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


class BaiDuHot(models.Model):
    """ 百度热榜 """

    key_word = models.CharField(max_length=225, verbose_name='关键词')
    href = models.CharField(max_length=225, verbose_name='地址')
    date = models.DateTimeField(max_length=225, verbose_name='日期', default=datetime.now)

    class Meta:
        db_table = 'baidu_hot'
        verbose_name = '百度热榜'
        verbose_name_plural = verbose_name