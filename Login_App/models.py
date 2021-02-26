from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='teacher_profile')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    profile_picture = models.ImageField(
        upload_to='profile_pic', blank=False)
    course_title = models.CharField(max_length=250)

    def __Str__(self):
        return self.user.username


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='student_profile')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    profile_picture = models.ImageField(
        upload_to='profile_pic', blank=False)
    email = models.EmailField()

    def __Str__(self):
        return self.user.username
