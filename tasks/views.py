from django.shortcuts import render, redirect, get_object_or_404
# Import generic and Task Model
from django.views import generic
from .models import Task
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy



class TaskListView(generic.ListView):
    model = Task
    template_name = 'index.html'
    # Display fields

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).values(
            'id', 'title', 'description', 'due_date', 'urgent', 'completed'
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

# Update Item


class EditTaskView(View):
    template_name = 'task_form.html'

    def get(self, request, task_id, *args, **kwargs):
        # Retrieve the task from the database using the task_id
        task = get_object_or_404(Task, id=task_id)

        # Pass the task details to the template for rendering the form
        context = {
            'task': task,
        }

        return render(request, self.template_name, context)

    def post(self, request, task_id, *args, **kwargs):
        # Retrieve the task from the database using the task_id
        task = get_object_or_404(Task, id=task_id)

        # Process the form submission here
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.urgent = request.POST.get('urgent', False) == 'on'
        task.save()

        return redirect('home')
