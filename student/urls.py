from django.contrib import admin
from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('enroll', views.enrollment_form, name='enroll'),
]
