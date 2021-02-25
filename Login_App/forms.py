from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Teacher, Student


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label="Username", widget=forms.TextInput(
        attrs={'placeholder': 'username'}))
    password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'password')
