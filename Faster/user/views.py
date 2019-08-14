from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import FormView
# Create your views here.


class RegisterView(FormView):
    pass


# 注销
def log_out(request):
    logout(request)
    return redirect('/')

