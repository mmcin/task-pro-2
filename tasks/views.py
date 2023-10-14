from django.shortcuts import render, redirect, get_object_or_404
# Import generic and Task Model
from django.views import generic
from .models import Task
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    template_name = 'index.html'
    # Display fields

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).values(
            'title', 'description', 'due_date', 'urgent', 'completed'
        )


class AddTaskView(View):
    template_name = 'add_task.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Process the form submission here
        title = request.POST.get('title')
        description = request.POST.get('description')
        urgent = request.POST.get('urgent', False) == 'on'

        # Create a new Task object
        task = Task(
            user=request.user,
            title=title,
            description=description,
            urgent=urgent
            )
        task.save()

        return redirect('home')


# Edit a task
def edit_task(request, task_id):
    return render(request, 'task_form.html')
