from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
import unittest


class TaskListViewTest(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.client = Client()

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # Manually check the template used
        self.assertIn(
            'index.html', [template.name for template in response.templates])
