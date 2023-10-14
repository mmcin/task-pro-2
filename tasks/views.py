from django.shortcuts import render
# Import generic and Task Model
from django.views import generic
from .models import Task


class TaskListView(generic.ListView):
    model = Task
    template_name = 'index.html'
    # Display fields

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).values(
            'title', 'description', 'due_date', 'urgent', 'completed'
        )


