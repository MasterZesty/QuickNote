from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterUserForm
from .forms import LoginUserForm
from django.http import HttpResponse


# Create your views here.
@login_required
def accounts_profile(request):
    
    user = request.user  # Get the authenticated user

    context = {
        'user': user
    }

    return render(request, 'profile.html',context)

def accounts_login(request):
    if request.method == 'POST':
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # verify a user credentials - checks the provided credentials against the credentials stored in the database
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, login successful!')
                # return render(request, 'authenticate/home_user.html',{'username': username}) # Redirect to user's page
                return redirect('accounts:profile') # Redirect to user's page
            else:
                form.add_error(None, 'Invalid username or password')
                
    else:
        form = LoginUserForm()

    return render(request,'login.html',{'form': form})

def accounts_logout(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return HttpResponse("<h1>'Hello World'</h1>")

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

