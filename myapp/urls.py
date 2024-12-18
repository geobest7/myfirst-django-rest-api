from django.urls import path
from .views import UserListView, UserDetailView, TaskListCreateView, TaskDetailView, AllTasksListView, TaskDeleteView, TaskUpdateView 

urlpatterns = [
    # Rutas para User
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    # Rutas para Task
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/all/', AllTasksListView.as_view(), name='all-task-list'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
]