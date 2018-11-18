from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def newSession(request):
    return None
