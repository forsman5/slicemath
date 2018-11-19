from django import forms

class NewSessionForm(forms.Form):
    yourName = forms.CharField(label='Your Name', max_length=100)
