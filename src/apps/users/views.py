from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import ExtendsUser
from .forms import sign_up

class user_home(ListView):
    model = ExtendsUser
    template_name = 'user_home.html'

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("..")

def register_request(request):
	if request.method == "POST":
		# Login
		sign_in_form = AuthenticationForm(request, data=request.POST)
		if sign_in_form.is_valid():
			username = sign_in_form.cleaned_data.get('username')
			password = sign_in_form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Você esta logado como {username}.")
				return redirect("..")
			else:
				messages.error(request,"Usuario ou Senha inválido.")
		else:
			messages.error(request,"Usuario ou Senha inválido.")
		# Register
		form = sign_up(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro bem sucedido." )
			return redirect("..")
		messages.error(request, "Registro Inválido")
	sign_up_form = sign_up()
	sign_in_form = AuthenticationForm()
	return render(  
               request=request,
               template_name="login.html",
               context={"register_form":sign_up_form,
                        "login_form":sign_in_form},)