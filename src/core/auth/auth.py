from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import sign_up


@login_required
def logout_request(request):
	logout(request)
	return HttpResponseRedirect('/account')


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
	# Form
	sign_up_form = sign_up()
	sign_in_form = AuthenticationForm()	
	# Return
	return render(  
               request=request,
               template_name="sign_in_&&_sign_up.html",
               context={"register_form":sign_up_form,
                        "login_form":sign_in_form,})

def recovery_pwd(request):
    return render(request, 'password_reset.html')

def recovery_pwd_done(request):
    return render(request, 'password_reset_done.html')