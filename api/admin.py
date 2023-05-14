from django.contrib import admin
from .models import ClientModel,ProjectModel

# Register your models here.



@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id' , 'client_name' , 'created_at' , 'created_by']


@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id' , 'project_name' , 'allocated_to']