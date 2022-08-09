from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("我们的第一个网页")

# Create your views here.
