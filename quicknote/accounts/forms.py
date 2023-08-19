from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# create login form
class LoginUserForm(AuthenticationForm):
    pass

# signup form
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    username = email
    class Meta:
        model =  User
        fields = (
                    'email',
                    'password1', 
                    'password2',
                    )