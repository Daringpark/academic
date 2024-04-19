from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserUpdateFrom
from .models import User

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('movies:index')

    form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

from django.contrib.auth import login as auth_login
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            auth_login(request, user)
            return redirect('movies:index')
    
    form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

from django.contrib.auth import logout as auth_logout
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('movies:index')

def update(request):
    user = User.objects.get(pk = request.user.pk)
    if request.method == "POST":
        # request.POST, instance = request.user
        form = CustomUserUpdateFrom(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', user.pk)

    # instance = request.user
    form = CustomUserUpdateFrom(instance = request.user)
    context = {
        'form' : form 
    }
    return render(request, 'accounts/update.html', context)

from django.contrib.auth import update_session_auth_hash
def password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile', form.user.pk)
    form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/password.html', context)

def delete(request):
    if request.method == 'POST':
        request.user.delete()
        auth_logout(request)
    return redirect('movies:index')

def profile(request, user_pk):
    user = User.objects.get(pk = user_pk)
    context = {
        'user' : user
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, user_pk):
    pass