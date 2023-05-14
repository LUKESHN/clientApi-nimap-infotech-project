
from rest_framework import viewsets

from .models import ClientModel,ProjectModel

from api.serializers import ClientSerializer,ProjectSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset= ClientModel.objects.all()
    serializer_class=ClientSerializer
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=ProjectModel.objects.all()
    serializer_class=ProjectSerializer