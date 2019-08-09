from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^gather/', ComprehensiveView.as_view(), name='gather'),
    url(r'^detail/', DetailView.as_view(), name='detail'),
    url(r'^recreation/', RecreationView.as_view(), name='recreation'),
    url(r'^$', IndexView.as_view(), name='index'),
]