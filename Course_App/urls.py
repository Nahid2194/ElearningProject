from django.contrib import admin
from django.urls import path, include
from Course_App import views
app_name = 'Course_App'
urlpatterns = [
    path('course-details/<slug:slug>/',
         views.courseDetails, name='course_details'),
    path('create_course/', views.create_course, name='create_course'),
    path('question/<pk>', views.question, name='question'),
    path('mycourse/', views.Mycourse.as_view(), name='mycourse'),

]
