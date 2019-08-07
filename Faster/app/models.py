from django.db import models
from datetime import datetime
from user.models import UserProfile
# Create your models here.


class ArticleType(models.Model):
    name = models.CharField(null=True, max_length=50, verbose_name='标签名')

    class Meta:
        db_table = 'article_type'


class Article(models.Model):
    """ 文章 """
    title = models.CharField(max_length=50, null=True, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    publish_time = models.DateTimeField(default=datetime.now, null=True, verbose_name='发布时间')
    update_time = models.DateTimeField(default=datetime.now, null=True, verbose_name='更新时间')
    comment_num = models.IntegerField(null=False, default=0, verbose_name='评论数')
    keep_num = models.IntegerField(null=False, default=0, verbose_name='收藏数')
    poll_num = models.IntegerField(null=False, default=0, verbose_name='点赞数')
    browse_num = models.IntegerField(null=False, default=0, verbose_name='浏览数')
    article_type = models.IntegerField(null=True)
    author = models.IntegerField(null=True)
    article_type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name='文章标签')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='作者')

    class Meta:
        db_table = 'article'
        verbose_name = '文章详情'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    content = models.CharField(null=True, max_length=255)
    date = models.DateTimeField(null=True, default=datetime.now)
    article = models.IntegerField(null=True)
    user = models.IntegerField(null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name


class Keep(models.Model):
    article = models.IntegerField(null=True)
    user = models.IntegerField(null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'keep'
        verbose_name = '收藏'
        verbose_name_plural = verbose_name


class Pool(models.Model):
    article = models.IntegerField(null=True)
    user = models.IntegerField(null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pool'
        verbose_name = '点赞'
        verbose_name_plural = verbose_name
