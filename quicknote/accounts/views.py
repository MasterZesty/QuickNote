from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm
from .forms import LoginUserForm
from django.http import Http404


# Create your views here.

def login(request):
    pass

def logout(request):
    pass

def password_change(request):
    pass

def password_reset(request):
    pass

def signup(request):
    # Create Account
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Log in the user
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Registration successful!")

                return redirect('https://www.google.com')  # Redirect to user's page
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegisterUserForm()

    return render(request, 'signup.html', {'form': form})

def delete(request):
    pass

