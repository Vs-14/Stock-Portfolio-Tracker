from django import forms

class basicForm(forms.Form):
    name = forms.CharField(label='Enter the company name:')