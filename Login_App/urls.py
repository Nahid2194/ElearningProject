from django.contrib import admin
from django.urls import path, include
from Login_App import views
app_name = 'Login_App'
urlpatterns = [
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('profile_teacher/', views.profile_teacher, name='profile_teacher'),
    path('student_profile/', views.student_profile, name='student_profile')
    path('student_login/', views.student_login, name='student_login'),

]
