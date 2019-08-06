from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^log_out/', log_out, name='log_out'),
]
