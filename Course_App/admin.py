from django.contrib import admin
from .models import Question, ReplyQuestion, Course
# Register your models here.
admin.site.register(Question)
admin.site.register(ReplyQuestion)
admin.site.register(Course)
