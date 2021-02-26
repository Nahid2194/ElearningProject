from django.db import models
from django.contrib.auth.models import User
from Login_App.models import Teacher, Student
from django.utils.text import slugify
import uuid

# Create your models here.


class Course(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name='course_teacher')
    course_title = models.CharField(max_length=250)
    course_picture = models.ImageField(
        verbose_name='Upload Course Picture', upload_to='course_picture')
    article = models.TextField(verbose_name='Course Article')
    quiz_link = models.URLField(verbose_name='Quiz Link')
    slug = models.SlugField(max_length=255, unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_title

    def save(self):
        self.slug = slugify(self.course_title + '-' + str(uuid.uuid4()))
        super(Course, self).save()


class Question(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='course_question')
    user = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='student_question')
    question = models.TextField()
    question_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-question_date']

    def __str__(self):
        return self.question
