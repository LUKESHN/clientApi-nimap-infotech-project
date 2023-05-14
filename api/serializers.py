
from rest_framework import serializers
from .models import ClientModel,ProjectModel



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = '__all__'

