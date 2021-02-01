from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ExtendsUser

class user_home(ListView):
    model = ExtendsUser
    template_name = 'user_home.html'