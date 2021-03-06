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


class SignupForm(UserCreationForm):
    username = forms.CharField(required=True, label="Username", widget=forms.TextInput(
        attrs={'placeholder': 'username'}))
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(
        attrs={'placeholder': 'Enter your Email'}))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))
    password2 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class TeacherEditForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude = ['user']


class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']
