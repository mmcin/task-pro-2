from django.db import models
# User Import
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    # Model representing tasks in the to-do list app.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_lenght=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    urgent = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
