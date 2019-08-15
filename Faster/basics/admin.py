from django.contrib import admin
from .models import RssSubscription
# Register your models here.


class RssSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['href', 'title', 'status']


admin.site.register(RssSubscription, RssSubscriptionAdmin)

