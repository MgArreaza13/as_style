from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.UserProfile.models import tb_profile
from django.forms import extras

class UsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username',]
		exclude = ['email',]


class ProfileForm(forms.ModelForm):
	
	class Meta:
		model = tb_profile
		fields = [
		'nameUser',
		'mailUser',
		'image',



		
		]
		labels = {
		'mailUser':'Correo Electronico', 
		'nameUser':'Ingrese su Nombre ',
		'image':'ingrese su imagen',

		
		}
		widgets = {}
          
		exclude = ['user','birthdayDate', ]  		
		
		
