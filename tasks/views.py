from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import ProjectForm
from .models import Project

# View for the home page
def home(request):
    return render(request, 'home.html')

# View for the signup page
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm()
    })
    else:
        # POST request
        if request.POST['password1'] == request.POST['password2']:
            #Resgister user
           try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('projects')
           except IntegrityError:
               return render(request, 'signup.html', {
                   'form': UserCreationForm(),
                   'error': 'Username is already exist'
                   })
        return render(request, 'signup.html', {
                   'form': UserCreationForm(),
                   'error': 'Passwords did not match'
                   })

def projects(request):

    projects = Project.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'projects.html', {
        'projects': projects
    
    }) 

def signout(request):
    logout(request)
    return redirect('home')   

def signin(request):

    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm()
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('projects')

def createProject(request):

    if request.method == 'GET':
        return render(request, 'createProject.html', {
            'form': ProjectForm
        })
    else:
        try:
            form =  ProjectForm(request.POST)
            newProject = form.save(commit=False)
            newProject.user = request.user
            newProject.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'createProject.html', {
                'form': ProjectForm(),
                'error': 'Please provide valid data, try again.'
            })

def tasks(request):
    return render(request, 'tasks.html')        