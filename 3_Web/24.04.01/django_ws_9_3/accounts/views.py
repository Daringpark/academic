from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('profiles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('profiles:index')

# 아래 두 함수 변경 필요
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profiles:index')
    else:
        form = CustomUserChangeForm(instance = request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)