from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import post

class blog_home(ListView):
    model = post
    template_name = 'article.html'

    

class detail_blog(DetailView):
    model = post
    template_name = 'post.html'

class add_post(CreateView):
    model = post
    template_name = 'novo_artigo.html'
    fields = ['background', 'title', 'summary', 'content']