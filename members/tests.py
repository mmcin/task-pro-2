from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from .forms import RegisterUserForm


class TestRegisterUserFormTest(unittest.TestCase):
    # Test username is required
    def test_username_is_required(self):
        form = RegisterUserForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())

    # test passwords are required to match
    def test_passwords_match_is_required(self):
        form = RegisterUserForm(
            {'username': 'testuser'},
            {'password1': 'password1'},
            {'password2': 'password123'},
            )
        self.assertFalse(form.is_valid())
  
    # test password must container number
    def test_passwords_number_required(self):
        form = RegisterUserForm(
            {'username': 'testuser'},
            {'password1': 'password'},
            {'password2': 'password'},
            )
        self.assertFalse(form.is_valid())
