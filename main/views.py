from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import models

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Main page', 'tasks': tasks})

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, '')
            return redirect('index')
    
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {form:form})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'False'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registartion successful.')
            return redirect('home')
        messages.error(request, 'Unsuccessful registration. Invalid information.')
    form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, "main/register.html", context)