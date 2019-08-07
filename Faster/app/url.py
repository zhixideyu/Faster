from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^details/', details, name='details'),
    url(r'^$', index, name='index'),
]