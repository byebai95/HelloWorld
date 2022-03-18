from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import register


def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'runoob.html', context)


def script(request):
    context = {'str': '<script>alert(\'Hello\')</script>>'}
    return render(request, 'script.html', context)


def iftest(request):
    context = {'age': -10}
    return render(request, 'if.html', context)


def fortest(request):
    list = {'a','b','c'}
    return render(request, 'for.html', {"list":list})


@register.filter
def get_range():
    return range(10)
