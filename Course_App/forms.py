from django import forms
from .models import ReplyQuestion, Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyQuestion
        fields = ['reply']
