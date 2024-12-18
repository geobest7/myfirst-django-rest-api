from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # Usar create_user para asegurarse de que la contraseña se cifre correctamente
        return user

class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Solo lectura del username del usuario

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'user']