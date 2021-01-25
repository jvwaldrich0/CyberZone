from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post

class blog_home(ListView):
    model = post
    template_name = 'article.html'