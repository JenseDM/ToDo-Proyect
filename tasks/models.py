from django.db import models
from django.contrib.auth.models import User

#Project model
class Project(models.Model):
    title = models.CharField(max_length=50)
    datecrated = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #The __str__ method is used to display the title of the project in the admin panel
    def __str__(self):
        return self.title + '- by ' + self.user.username
#Task model
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    datecrated = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    #The __str__ method is used to display the title of the task in the admin panel
    def __str__(self):
        return self.title