from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post

# Create your views here.
#def blog_home(request):
#    return render(request, 'article.html')

class blog_home(ListView):
    model = post
    template_name = 'article.html'