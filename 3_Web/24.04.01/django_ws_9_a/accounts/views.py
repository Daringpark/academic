from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user
from .forms import CustomCreationForm, CustomChangeForm
from django.contrib.auth.forms import AuthenticationForm
# from .forms import LoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')

# signup
def signup(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = CustomCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def update(request):
    if request.method == 'POST':
        form = CustomChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = CustomChangeForm(instance = request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)