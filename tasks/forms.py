from django.forms import ModelForm
from .models import Project, Task

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']