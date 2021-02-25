from django.contrib import admin
from django.urls import path, include
from Login_App import views
app_name = 'Login_App'
urlpatterns = [
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('profile_teacher/', views.profile_teacher, name='profile_teacher'),
    path('profile_student/', views.profile_student, name='profile_student'),
    path('student_login/', views.student_login, name='student_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('signup_teacher/', views.signup_teacher, name='signup_teacher'),

]
