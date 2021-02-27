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
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course_obj = form.save(commit=False)
            course_obj.teacher = request.user.teacher_profile
            title = course_obj.course_title
            course_obj.slug = slugify(
                title.replace(" ", "-") + str(uuid.uuid4()))
            course_obj.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'Course_App/create_course.html', context={'form': form})


@login_required
def courseDetails(request, slug):
    course = Course.objects.get(slug=slug)
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user.student_profile
            question.course = course
            question.save()
            return HttpResponseRedirect(reverse('Course_App:course_details', kwargs={'slug': slug}))
    return render(request, 'Course_App/course_details.html', context={'course': course, 'form': form})


@login_required
def question(request, pk):
    form = ReplyForm()
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.question = question
            reply.save()
            return HttpResponseRedirect(reverse('Course_App:question',kwargs={'pk':pk}))
    return render(request, 'Course_App/question.html', context={'form': form,'question':question})


class Mycourse(LoginRequiredMixin,TemplateView):
    template_name = 'Course_App/mycourse.html'