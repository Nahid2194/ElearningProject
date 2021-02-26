from django.contrib import admin
from django.urls import path, include
from Course_App import views
app_name = 'Course_App'
urlpatterns = [
    path('create_course/', views.create_course, name='create_course')
]
