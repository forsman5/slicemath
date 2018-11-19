from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import forms
from . import models

def index(request):
    if request.method == 'POST' or request.method == 'post':
        if 'createForm' in request.POST:
            # create a form instance and populate it with data from the request:
            form = forms.NewSessionForm(request.POST)

            # check whether it's valid:
            if form.is_valid():
                # create a new session
                session = models.Session()
                session.save()

                member = models.Member.objects.create(name=form.cleaned_data['name'], session=session)

                # return the rendered, new session page
                return HttpResponseRedirect(reverse('session', args = [session.id]))

            else:
                print("FAIL")
                # TODO: print an error and request resumbit
                pass
        else:
            # joinForm
            form = forms.JoinSessionForm(request.POST)

            # check whether it's valid:
            if form.is_valid():
                # read the session from db
                session = Session.objects.get(pk=form.cleaned_data['sessionCode'])

                # create the new member of that session
                member = models.Member.objects.create(name=form.cleaned_data['name'], session=session)

                # return the rendered, new session page
                return HttpResponseRedirect(reverse('session', args = [sessionId]))

            else:
                print("FAIL2")
                # TODO: print an error and request resumbit
                pass
    else:
        joinForm = forms.JoinSessionForm()
        createSession = forms.NewSessionForm()

        return render(request, 'index.html', {'createForm': createSession, 'joinForm': joinForm})

def session(request, id):
    # get session from db
    session = models.Session.objects.get(pk=id)

    return render(request, 'session.html', {'session': session})
