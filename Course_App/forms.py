from django import forms
from .models import ReplyQuestion, Question, Course


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyQuestion
        fields = ['reply']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_title', 'course_picture', 'article', 'quiz_link', ]
