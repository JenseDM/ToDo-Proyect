from django.contrib import admin
from .models import Project, Task    
'''
class ProjectsAdmin(admin.ModelAdmin):
    readonly_fields = ('completed', )

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('completed', )
'''
# Register your models here.
admin.site.register(Project)
admin.site.register(Task)