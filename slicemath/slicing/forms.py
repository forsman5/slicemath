from django import forms

class NewSessionForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=50)

class JoinSessionForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=50)
    sessionCode = forms.CharField(label='Session Code', max_length=50)
