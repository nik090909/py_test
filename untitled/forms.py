from django import forms

class MyForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    #address = forms.CharField(label='Address')
    #book = forms.CharField(label='Book')