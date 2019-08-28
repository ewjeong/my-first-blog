from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def today(request):
    message = '오늘은 화요일'
    return HttpResponse(message)

def todo(request):
    message = '장고스터디 하는 날!'
    return HttpResponse(message)
