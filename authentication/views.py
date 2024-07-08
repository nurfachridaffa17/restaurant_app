from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {'form': UserCreationForm})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return HttpResponseRedirect('/login')
    else:
        form = UserCreationForm()


def login(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {'form': AuthenticationForm})
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return "Berhasil Login" 
    else:
        form = AuthenticationForm()

def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
