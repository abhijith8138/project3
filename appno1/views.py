from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def appno1(request):
    return HttpResponse('<h1> hi abhijith</h1\>')


def appno1second(request):
    return HttpResponse('<h1> second appno1</h1>' )