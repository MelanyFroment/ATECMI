# core/forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    company = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    consent = forms.BooleanField() 