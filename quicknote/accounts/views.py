'''
accounts app  - view module
'''

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm
from .forms import LoginUserForm

# Create your views here.
@login_required
def accounts_profile(request):
    '''
    View function to handle user account profile.
    '''
    return redirect('/notes/')

def accounts_login(request):
    '''
    View function to handle user login.
    '''
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # verify a user credentials - checks the provided
            # credentials against the credentials stored in the database
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, login successful!')
                return redirect('accounts:profile') # Redirect to user's page
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginUserForm()

    return render(request,'login.html',{'form': form})

def accounts_logout(request):
    '''
    handle user account logout
    '''
    logout(request)
    messages.success(request, ("You Were Logged Out!"))
    return redirect('accounts:login') # Redirect to login page

def accounts_password_change(request):
    '''
    handle user account password change
    '''

def accounts_password_reset(request):
    '''
    handle user account password reset
    '''

def accounts_signup(request):
    ''''
    handle user account signups
    '''
    # Create Account
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                messages.success(request, "Registration successful!")

                return redirect('accounts:profile')  # Redirect to user's page
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegisterUserForm()

    return render(request, 'signup.html', {'form': form})

def accounts_delete(request):
    '''
    handle user account deletion
    '''
