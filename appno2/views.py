from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def appno2(request):
    return HttpResponse('<h1> second app appno2/h1\>')


def appno2second(request):
    return HttpResponse('<h1> second appno2</h1>' )
