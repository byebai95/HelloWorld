import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import register
from environs import Env


def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'runoob.html', context)


def script(request):
    context = {'scriptStr': '<script>alert(\'Hello\')</script>>'}
    return render(request, 'script.html', context)


def iftest(request):
    context = {'age': -10}
    return render(request, 'if.html', context)


def fortest(request):
    lst = {'a', 'b', 'c'}
    return render(request, 'for.html', {"list": lst})


def href(request):
    request.encoding = 'utf-8'
    dct = {'hrefStr': "<a href='https://www.runoob.com/'>点击跳转</a>"}
    return render(request, 'href.html', dct)


def envtest(request):
    env = Env()
    host = env.str("HOST")
    return render(request, 'env.html', {"HOST": host})
