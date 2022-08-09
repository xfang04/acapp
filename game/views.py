from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    line1 = '<h1 style="text-align:center">我们的第一个网页</h1> '
    return HttpResponse(line1)

# Create your views here.
