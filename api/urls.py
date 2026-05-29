from django.urls import path
from .views import task_list_create, task_detail_update_delete

urlpatterns = [
    # URL for getting all tasks or creating a new one
    path('tasks/', task_list_create, name='task_list_create'),
    # URL for acting on a specific task using its ID number (pk)
    path('tasks/<int:pk>/', task_detail_update_delete, name='task_detail_update_delete'),
]