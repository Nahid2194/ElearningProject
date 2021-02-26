from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Teacher, Student
from .forms import LoginForm, SignupForm, StudentEditForm, TeacherEditForm
# Create your views here.


def homepage(request):
    return render(request, 'home.html', context={})


def teacher_login(request):
    name = 'Teacher Login Form'
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
    return render(request, 'Login_App/login.html', context={'form': form, 'teacher': True, 'name': name})


@login_required
def profile_teacher(request):
    return render(request, 'Login_App/profile.html', context={'teacher': True})


def student_login(request):
    name = 'Student Login Form'
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Login_App:profile_student'))
    return render(request, 'Login_App/login.html', context={'form': form, 'name': name})


@login_required
def profile_student(request):
    return render(request, 'Login_App/profile.html', context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def signup_teacher(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile_teacher = Teacher(user=user)
            profile_teacher.save()
            return HttpResponseRedirect(reverse('Login_App:teacher_login'))

    return render(request, 'Login_App/signup.html', context={'form': form, 'teacher': True, 'name': 'Teacher'})


def signup_student(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile_student = Student(user=user)
            profile_student.save()
            return HttpResponseRedirect(reverse('Login_App:student_login'))
    return render(request, 'Login_App/signup.html', context={'form': form, 'name': 'Student'})


@login_required
def edit_student(request):
    student = Student.objects.get(user=request.user)
    form = StudentEditForm(instance=student)
    if request.method == 'POST':
        form = StudentEditForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return HttpResponseRedirect(reverse('Login_App:profile_student'))
    return render(request, 'Login_App/edit_profile.html', context={'form': form, 'name': 'Update'})


@login_required
def edit_teacher(request):
    teacher = Teacher.objects.get(user=request.user)
    form = TeacherEditForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherEditForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.save()
            return HttpResponseRedirect(reverse('Login_App:profile_teacher'))
    return render(request, 'Login_App/edit_profile.html', context={'form': form, 'name': 'Update', 'teacher': True})
