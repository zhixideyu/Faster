from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_active', 'last_login']
    search_fields = ['username']
    list_filter = ['username']


admin.site.register(UserProfile, UserProfileAdmin)
