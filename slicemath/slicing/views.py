from django.shortcuts import render
from django.http import HttpResponse
from . import forms

def index(request):
    createSession = forms.NewSessionForm()

    return render(request, 'index.html', {'form': createSession})

def session(request):
    pass

def newSession(request):
    # create a form instance and populate it with data from the request:
    form = forms.createSession(request.POST)

    # check whether it's valid:
    if form.is_valid():
        # create a new session
        session = None

        # create the new member of that session

        # return the rendered, new session page
        return render(request, 'session.html', {'session': session})

    else:
        # TODO: redirect
        pass
