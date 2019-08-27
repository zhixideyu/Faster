from django.db import models
from datetime import datetime

# Create your models here.


class RssInfoSpider(models.Model):

    STATUS_CHOICES = (
        ('d', '禁用'),
        ('p', '正常'),
    )

    url = models.CharField(max_length=255, verbose_name='链接', null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p', verbose_name='规则状态')
    feed_title_rule = models.CharField(max_length=255, verbose_name='标题正则', null=True, default='<title>(.*?)</title>')
    connect_rule = models.TextField(verbose_name='内容正则', blank=False, null=True)
    next_href_rule = models.CharField(max_length=255, blank=True, null=True, verbose_name='下一页正则')
    encode = models.CharField(max_length=20, verbose_name='编码格式', blank=True, null=True)
    xml_name = models.CharField(max_length=50, verbose_name='xml文件名', blank=False, null=True)
    add_time = models.DateTimeField(default=datetime.now, blank=True, null=False, verbose_name='添加时间')
    type = models.CharField(max_length=20, default='html', blank=False, null=True, verbose_name='数据类型')

    class Meta:
        db_table = 'rss_info_spider'
        verbose_name = '用户规则'
        verbose_name_plural = verbose_name


class RssResultInfo(models.Model):

    feed_url = models.CharField(max_length=255, blank=False, null=True)
    feed_titile = models.CharField(max_length=255, blank=False, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    publish_time = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, blank=False, null=True)
    url = models.CharField(max_length=255, blank=False, null=True)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    spider_time = models.DateTimeField(default=datetime.now, blank=True, null=True, verbose_name='爬取时间')
    xml_name = models.ForeignKey(RssInfoSpider, on_delete=models.CASCADE, verbose_name='xml文件', blank=False, null=True)

    class Meta:
        db_table = 'rss_result_info'
        verbose_name = '根据RSS规则爬取的内容'
        verbose_name_plural = verbose_name
