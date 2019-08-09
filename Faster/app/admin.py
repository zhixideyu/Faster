from django.contrib import admin
from .models import Article, ArticleType, ArticleClass
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_time', 'browse_num', 'author']
    search_fields = ['title', 'publish_time', 'browse_num', 'author']
    list_filter = ['title', 'publish_time', 'browse_num', 'author']


admin.site.register(Article, ArticleAdmin)


class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(ArticleType, ArticleTypeAdmin)


class ArticleClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']


admin.site.register(ArticleClass, ArticleClassAdmin)
