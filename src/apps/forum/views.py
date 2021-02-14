from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import question

class forum_home(ListView):
    model = question
    template_name = 'forum.html'