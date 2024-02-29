from django.db import IntegrityError
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import ProjectForm, TaskForm
from .models import Project, Task
from django.contrib.auth.decorators import login_required

# View for the home page
def home(request):
    return render(request, 'home.html', {
        'user': request.user
    })

# View for the signup page
def signup(request):
    # GET request
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

# View for the signout page
@login_required
def signout(request):
    # POST request
    logout(request)
    return redirect('home')   

# View for the signin page
def signin(request):
    # GET request
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm()
    })
    else:
        # POST request
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Username or password is incorrect'
            })
        else:
            # Login user
            login(request, user)
            return redirect('projects')

# View for the project form page
@login_required
def createProject(request):
    # GET request
    if request.method == 'GET':
        return render(request, 'createProject.html', {
            'form': ProjectForm
        })
    else:
        # POST request
        try:
            # Create project
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

# View for the projects page
@login_required
def projects(request):
    # GET request
    projects = Project.objects.filter(user=request.user, completed=False)
    if projects.count() == 0:
        return render(request, 'projects.html', {
            'message': 'There are no pending projects.'
        })
    return render(request, 'projects.html', {
        'projects': projects,
        'message': 'Your projects are here.'
    }) 

# View for the create task form page
@login_required
def createTask(request, project_id):
    # GET request
    if request.method == 'GET':
        return render(request, 'createTask.html', {
            'form': TaskForm,
        })
    else:
        # POST request
        try:
            # Create task
            form =  TaskForm(request.POST)
            newTask = form.save(commit=False)
            newTask.project = Project.objects.get(pk=project_id)
            newTask.save()
            return redirect('tasks', project_id=project_id)
        except ValueError:
            return render(request, 'createTask.html', {
                'form': TaskForm(),
                'error': 'Please provide valid data, try again.'
            })

# View for the tasks page
@login_required
def tasks(request, project_id):
    # GET request
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project_id, completed=False)
    
    if tasks.count() == 0:
        # If there are no tasks
        return render(request, 'tasks.html', {
            'message': 'You have not created any tasks yet.',
            'project_id': project_id,
            'project': project
        })
    return render(request, 'tasks.html', {
        'tasks': tasks,
        'project_id': project_id,
        'project': project
    })        

# View for the task detail page
@login_required
def taskDetail(request, idtask):
    # GET request
    task = get_object_or_404(Task, pk=idtask)
    return render(request, 'taskDetail.html', {
        'task': task
    })

# View for complete task
@login_required
def completeTask(request, idtask): 
   task =  get_object_or_404(Task, pk=idtask)
   if request.method == 'POST':
       task.completed = True
       task.save()
       finished_tasks = Task.objects.filter(project=task.project, completed=True).count()
       all_tasks = Task.objects.filter(project=task.project).count()
        # If all tasks are completed, the project is completed
       if finished_tasks == all_tasks:
            project = Project.objects.get(pk=task.project.id)
            project.completed = True
            project.delete()
            return redirect('projects')
       return redirect('tasks', project_id = task.project.id)

# View for delete task
@login_required   
def deleteTask(request, idtask):
    task =  get_object_or_404(Task, pk=idtask)
    if request.method == 'POST':
         task.delete()
         finished_tasks = Task.objects.filter(project=task.project, completed=True).count()
         all_tasks = Task.objects.filter(project=task.project).count()
         # If all tasks are completed, the project is completed
         if finished_tasks == all_tasks:
            project = Project.objects.get(pk=task.project.id)
            project.completed = True
            project.delete()
            return redirect('projects')
         return redirect('tasks', project_id = task.project.id)

# View for delete project
@login_required
def deleteProject(request, project_id):
    project =  get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
         project.delete()
         return redirect('projects')
    