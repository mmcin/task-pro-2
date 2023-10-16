from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Styling the User Registration Form


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}),
        )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Confirm Password '}),
        )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
