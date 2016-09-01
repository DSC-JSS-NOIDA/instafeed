from django import forms
from django.forms import ModelForm
from .models import *

class Login(forms.Form):
	username = forms.CharField(label='Username', max_length=150)
	password = forms.CharField(label='Passowrd', max_length=32, widget=forms.PasswordInput)


class SocietyForm(ModelForm):
	class Meta:
		model = Society
		exclude = ['society_user']
