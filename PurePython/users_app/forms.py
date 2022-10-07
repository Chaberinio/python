from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=256,widget=forms.PasswordInput())

class RegisterUser(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=256,widget=forms.PasswordInput())
    email = forms.EmailField(max_length=128)