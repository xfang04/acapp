# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    line1 = '<h1 style="text-align:center">我们的第一个网页</h1>'
    line2 = '<hr>'
    line3 = '<a href="/play/">进入游戏界面</a>'
    return HttpResponse(line1 + line2 + line3)


def play(request):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<a href="/">返回主界面</a>'
    return HttpResponse(line1 + line2)


# Create your views here.
