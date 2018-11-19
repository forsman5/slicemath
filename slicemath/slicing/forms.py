from django import forms

class NewSessionForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))

class JoinSessionForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
    sessionCode = forms.CharField(label='Session Code', max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
