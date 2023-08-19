from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm
from .forms import LoginUserForm
from django.http import Http404


# Create your views here.
@login_required
def accounts_profile(request):
    
    user = request.user  # Get the authenticated user

    context = {
        'user': user
    }

    return render(request, 'profile.html',context)

def accounts_login(request):
    pass

def accounts_logout(request):
    pass

def accounts_password_change(request):
    pass

def accounts_password_reset(request):
    pass

def accounts_signup(request):
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
    pass

