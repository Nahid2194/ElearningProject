from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Teacher(models.Model):
    user = models.oneToOneField(
        User, on_delete=models.CASCADE, related_name='teacher_profile')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    course_title = models.CharField(max_length=250)

    def __Str__(self):
        return self.user.username
