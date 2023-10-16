from django.contrib.auth.models import User
from django.test import TestCase
from .models import Task
import unittest


class TestTaskModel(unittest.TestCase):

    def test_urgent_defaults_to_false(self):
        # Create a user
        user = User.objects.create(username='Change Name 3')

        # Create a task associated with the user
        task = Task.objects.create(title='Test model', user=user)

        # Assert that urgent is False
        self.assertFalse(task.urgent)
        # Asser that completed is false
        self.assertFalse(task.completed)
