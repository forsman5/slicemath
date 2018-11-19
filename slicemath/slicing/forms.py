from django import forms

class NewSessionForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=50, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Dwayne Haskins'}))

class JoinSessionForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=50, widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Dwayne Haskins'}))
    sessionCode = forms.CharField(label='Session Code', max_length=50, widget=forms.TextInput(attrs={'class': "form-control"}))
