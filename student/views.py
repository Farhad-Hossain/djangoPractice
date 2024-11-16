from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from home.utils import hx_render

def enrollment_form(request):    
    return hx_render(request, 'student/enrollment_form.html', {"title": 'Student Enrollment form'})
