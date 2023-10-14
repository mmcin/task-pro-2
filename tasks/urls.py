from . import views
from django.urls import path
from .views import AddTaskView, edit_task


urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('edit/<task_id>', edit_task, name='edit'),
]
