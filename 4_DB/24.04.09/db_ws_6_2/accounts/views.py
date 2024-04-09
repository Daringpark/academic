from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm 

# Create your views here.
def login(request):
    if request.method == "POST":
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            auth_login(request, loginForm.get_user())
            return redirect('libraries:index')
    loginForm = AuthenticationForm()
    context = {
        'loginForm' : loginForm
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('libraries:index')

def signup(request):
    if request.method == "POST":
        signupForm = CustomUserCreationForm(request.POST)
        if signupForm.is_valid():
            user = signupForm.save()
            auth_login(request, user)
        return redirect('libraries:index')
    signupForm = CustomUserCreationForm()
    context = {
        'signupForm' : signupForm
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def signout(request):
    request.user.delete()
    return redirect('libraries:index')