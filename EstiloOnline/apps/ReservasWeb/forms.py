from django import forms
from django.forms import ModelForm, Textarea ,Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.ReservasWeb.models import tb_reservasWeb
from django.forms import extras



class ReservasWebForm(forms.ModelForm):
	
	class Meta:
		model = tb_reservasWeb
		fields = [
		'mail',
		'nombre',
		'telefono',
		
		
		
		
		]
		exclude = ['dateTurn', 'HoraTurn',"statusTurn", 'montoAPagar', 'description','servicioPrestar', 'isPay']

		labels = {
		'mail':'ingrese su correo', 
		'nombre': 'ingrese su nombre',
		'telefono':'ingrese su telefono de contacto',
		
		
		}

		widgets = {

		

		
		}



class EditReservaWebForm(forms.ModelForm):
	
	class Meta:
		model = tb_reservasWeb
		fields = [
		'statusTurn',
		
		
		]
		exclude = ['dateTurn', 'servicioPrestar', 'HoraTurn',  'mail', 'client', 'nombre', 'telefono', 'isPay']

		labels = {
		'statusTurn':'Estatus',
		
		
		}
		widgets = {
		'statusTurn':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione el status'}),
		}