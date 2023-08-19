from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models



# create login form
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

# signup form
class RegisterUserForm(UserCreationForm):
    class Meta:
        model =  User
        fields = ("username", "password1", "password2")