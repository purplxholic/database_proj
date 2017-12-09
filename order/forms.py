from django import forms

from django.contrib.auth.models import User


class OrderForm(forms.Form):
    sid = forms.CharField(max_length=10, required=True, help_text='Example:0000000045')
    uid = forms.CharField(max_length=10, required=True, help_text='Example:5507545360')

    #