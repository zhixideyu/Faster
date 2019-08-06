from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.


# 注销
def log_out(request):
    logout(request)
    return redirect('/')

