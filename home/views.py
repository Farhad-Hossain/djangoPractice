from django.shortcuts import render
from .utils import *

def home_page(request):
    return render(request, 'home/home_page.html')

def dashboard(request):
    return hx_render(request, 'home/dashboard.html', {
        "title": 'Dashboard'
    })