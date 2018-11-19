from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import forms

def index(request):
    createSession = forms.NewSessionForm()

    return render(request, 'index.html', {'form': createSession})

def session(request, id):
    # get session from db
    session = None

    return render(request, 'session.html', {'session': session})

def newSession(request):
    # create a form instance and populate it with data from the request:
    form = forms.NewSessionForm(request.POST)

    # check whether it's valid:
    if form.is_valid():
        # create a new session
        sessionId = 0

        # create the new member of that session

        # return the rendered, new session page
        return HttpResponseRedirect(reverse('session', args = [sessionId]))

    else:
        # TODO: redirect
        pass
