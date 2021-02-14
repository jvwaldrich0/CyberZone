from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import ExtendsUser
from apps.blog.models import models, post
from .form import UserEditForm, UserPasswordForm
from django.contrib.auth import views as auth_views


class user_home(DetailView):
    model = ExtendsUser
    template_name = 'user_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = post.objects.all()
        return context


class update_user_settings(UpdateView):
    form_class = UserEditForm
    template_name = 'edit_user_settings.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
    
class update_user(UpdateView):
    model = ExtendsUser
    template_name = 'edit_user.html'
    success_url = reverse_lazy('home')
    fields = ['profile_background', 'profile_picture', 'bio', 'gender', ]
    

class update_user_password(auth_views.PasswordChangeView):
    form_class = UserPasswordForm
    success_url = reverse_lazy('password_success')
    
def update_user_password_success(request):
    return render(request, 'password_success.html')