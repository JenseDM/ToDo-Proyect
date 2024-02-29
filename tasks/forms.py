from django.forms import ModelForm
from .models import Project, Task

class ProjectForm(ModelForm):   # Create a form from the Project model
    class Meta:
        model = Project
        fields = ['title']

class TaskForm(ModelForm):  # Create a form from the Task model
    class Meta:
        model = Task
        fields = ['title', 'description']