from django.db import models

# Create your models here.



class ClientModel(models.Model):
    client_name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.client_name


class ProjectModel(models.Model):
    project_name = models.CharField(max_length=100)
    allocated_to = models.ForeignKey(ClientModel , on_delete=models.CASCADE)

