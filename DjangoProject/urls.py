"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('projects/', views.projects, name="projects"),
    path('logout/', views.signout, name="logout"),
    path('signin/', views.signin, name="signin"),
    path('createProject/', views.createProject, name="createProject"),
    path('createTask/<int:project_id>/', views.createTask, name="createTask"),
    path('tasks/<int:project_id>/', views.tasks, name="tasks"),
    path('taskDetail/<int:idtask>/', views.taskDetail, name="taskDetail"),
    path('taskDetail/<int:idtask>/complete', views.completeTask, name="completeTask"),
    path('taskDetail/<int:idtask>/delete', views.deleteTask, name="deleteTask"),
]
