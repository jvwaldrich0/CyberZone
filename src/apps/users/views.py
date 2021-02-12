from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import ExtendsUser

class user_home(DetailView):
    model = ExtendsUser
    template_name = 'user_home.html'
    
