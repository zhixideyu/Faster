from django.contrib import admin
from .models import RssResultInfo, RssInfoSpider
# Register your models here.


class RssInfoSpiderAdmin(admin.ModelAdmin):
    list_display = ['url', 'encode', 'xml_name', 'add_time']
    search_fields = ['url', 'xml_name', 'add_time']


admin.site.register(RssInfoSpider, RssInfoSpiderAdmin)