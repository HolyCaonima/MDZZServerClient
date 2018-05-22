# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect


def check_login(request):
    if request.user.is_authenticated:
        user = request.user

    else:
        redirect('app/user_login')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Login')
        else:
            return HttpResponse('fa')


def zzz(request):
    if request.user.is_authenticated:
        return HttpResponse('Ok')
    else:
        return HttpResponse('faaaa')



