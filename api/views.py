
from rest_framework import viewsets
from django.shortcuts import render
from .models import ClientModel,ProjectModel
from django.contrib.auth.decorators import login_required
from api.serializers import ClientSerializer,ProjectSerializer
from rest_framework.decorators import api_view

from rest_framework.decorators import login_required
from rest_framework.response import Response

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset= ClientModel.objects.all()
    serializer_class=ClientSerializer
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=ProjectModel.objects.all()
    serializer_class=ProjectSerializer


@login_required(login_url='/project/login/')
def project(request):
    user=request.user
    return render(request)

@api_view(['GET'])
def current_user(request):
    serializer=UserSerializer(request.user)
    return Response(serializer.data)
def put_user(request):
    list_display={
        "id":"1",
        "client_name":"xyz",
        "created_at":"2023-12",
        "created_by":"xyz",

    }
    Response=request.client.put(
        request.id,
        list_display=list_display
    )
    return render(request)