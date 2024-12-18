from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)  # Título de la tarea
    description = models.TextField()  # Descripción de la tarea
    completed = models.BooleanField(default=False)  # Estado de la tarea
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)  # Relación con User
    
    def __str__(self):
        return self.title
