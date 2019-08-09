from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^detail_api/', detail_api, name='detail_api'),
]