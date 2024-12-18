from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, UserSerializer

# Vistas para los usuarios
class UserListView(generics.ListCreateAPIView):
    """
    Lista todos los usuarios o permite crear nuevos usuarios.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Detalles de un usuario, permite actualizar o eliminar un usuario.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Vistas para las tareas (Task)
class TaskListCreateView(generics.ListCreateAPIView):
    """
    Lista todas las tareas o permite crear nuevas tareas.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveAPIView):
    """
    Recupera una tarea específica.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AllTasksListView(generics.ListAPIView):
    """
    Enumera todas las tareas.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDeleteView(generics.DestroyAPIView):
    """
    Elimina una tarea específica.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_destroy(self, instance):
        instance.delete()

class TaskUpdateView(generics.UpdateAPIView):
    """
    Actualiza una tarea específica.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
