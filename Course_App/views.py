from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
import uuid
from django.utils.text import slugify
from Login_App.models import Teacher, Student
from .models import Course, Question, ReplyQuestion
from .forms import ReplyForm, QuestionForm, CourseForm

# Create your views here.


def homepage(request):
    courses = Course.objects.all()
    return render(request, 'home.html', context={'courses': courses})


@login_required
def create_course(request):
    form = CourseForm()

    return render(request, 'Course_App/create_course.html', context={'form': form})
