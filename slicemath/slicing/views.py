from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {})

def newSession(request):
    # create a new session
    session = None

    # create the new member of that session

    # return the rendered, new session page
    return render(request, 'session.html', {'session': session})
    
