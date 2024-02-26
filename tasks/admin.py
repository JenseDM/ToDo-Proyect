from django.contrib import admin
from .models import Project    

class ProjectsAdmin(admin.ModelAdmin):
    readonly_fields = ('datecrated', )

# Register your models here.
admin.site.register(Project, ProjectsAdmin)