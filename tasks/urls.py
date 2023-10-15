from . import views
from django.urls import path
from .views import AddTaskView, EditTaskView, DeleteTaskView, home


urlpatterns = [
    path('', home, name='home'),
    path('tasks/', views.TaskListView.as_view(), name='view_tasks'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('edit/<task_id>', EditTaskView.as_view(), name='edit'),
    path('delete/<task_id>', DeleteTaskView.as_view(), name='delete')
]
