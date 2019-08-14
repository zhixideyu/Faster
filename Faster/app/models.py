from django.db import models
from datetime import datetime
from django.urls import reverse
from user.models import UserProfile
from ckeditor.fields import RichTextField
from django.db.models.fields import DateTimeField

from django.db.models.fields.related import ManyToManyField
# Create your models here.


class ArticleCategory(models.Model):
    name = models.CharField(null=True, max_length=50, unique=True, verbose_name='分类名')
    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name='父级分类')
    slug = models.SlugField(default='no-slug', max_length=60, blank=True)

    class Meta:
        # 排序
        ordering = ['name']
        db_table = 'article_category'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ArticleType(models.Model):
    name = models.CharField(null=True, max_length=50, verbose_name='标签名')

    class Meta:
        db_table = 'article_type'
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    """ 文章 """

    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )

    def to_dict(self, fields=None, exclude=None):
        """ 将model对象转换为dict """
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, ManyToManyField):
                value = [i.id for i in value] if self.pk else None
            if isinstance(f, DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
            data[f.name] = value
        return data

    """ 文章 """
    title = models.CharField(max_length=50, null=True, verbose_name='标题')
    content = RichTextField(verbose_name='内容')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p', verbose_name='文章状态')
    publish_time = models.DateTimeField(default=datetime.now, null=True, verbose_name='发布时间')
    update_time = models.DateTimeField(default=datetime.now, null=True, verbose_name='更新时间')
    comment_num = models.IntegerField(null=False, default=0, verbose_name='评论数')
    keep_num = models.PositiveIntegerField(null=False, default=0, verbose_name='收藏数')
    poll_num = models.PositiveIntegerField(null=False, default=0, verbose_name='点赞数')
    browse_num = models.PositiveIntegerField(null=False, default=0, verbose_name='浏览数')
    article_tags = models.ManyToManyField(ArticleType, verbose_name='文章标签', blank=False)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='作者', blank=False, null=False)
    article_category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='文章分类', blank=False, null=False)

    class Meta:
        ordering = ['-publish_time']
        db_table = 'article'
        verbose_name = '文章详情'
        verbose_name_plural = verbose_name

    def viewed(self):
        """ 浏览数 += 1 """
        self.browse_num += 1
        self.save(update_fields=['browse_num'])

    def next_article(self):
        """ __gt 大于 下一篇文章 """
        return Article.objects.filter(id__gt=self.id, status='p').order_by('id').first()

    def prev_article(self):
        """ __lt 小于 上一篇文章 """
        return Article.objects.filter(id__lt=self.id, status='p').first()

    def get_absolute_url(self):

        return reverse('detail', kwargs={
            'article_id': self.id
        })


class Comment(models.Model):
    """ 评论 """

    content = models.CharField(null=True, max_length=255)
    date = models.DateTimeField(null=True, default=datetime.now)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name


class Keep(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'keep'
        verbose_name = '收藏'
        verbose_name_plural = verbose_name


class Pool(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        db_table = 'pool'
        verbose_name = '点赞'
        verbose_name_plural = verbose_name
