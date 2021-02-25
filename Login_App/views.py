from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Teacher, Student
from .forms import LoginForm, SignUpForm, EditStudentForm, EditTeacherForm
# Create your views here.


def homepage(request):
    return render(request, 'Login_App/login.html', context={})


def teacher_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Login_App:profile_teacher'))
    return render(request, 'Login_App/login.html', context={'form': form})


def profile_teacher(request):
    return render(request, 'Login_App/profile_teacher.html', context={})
