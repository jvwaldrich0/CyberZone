from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.users.models import ExtendsUser

class sign_up(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(sign_up, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user