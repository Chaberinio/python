from django import forms
from django.core.validators import MinLengthValidator
from django.http import HttpResponse
from django.shortcuts import render


class LoginForm(forms.Form):
    login = forms.CharField(label='Twój login', max_length=100)
    password = forms.CharField(label='Twóje hasło', max_length=128, widget=forms.PasswordInput(),validators=[MinLengthValidator(limit_value=3)])
