from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post
from .forms import postForm

class blog_home(ListView):
    model = post
    template_name = 'article.html'
    ordering = ['-published_at']

class detail_blog(DetailView):
    model = post
    template_name = 'post.html'

class add_post(CreateView):
    model = post
    template_name = 'novo_artigo.html'
    form_class = postForm
    
class edit_post(UpdateView):
    model = post
    template_name = 'editar_artigo.html'
    fields = ['title', 'content', 'background', 'summary']
    
class delete_post(DeleteView):
    model = post
    template_name = 'delete_post.html'
    fields = '__all__'
    success_url = reverse_lazy('blog')