from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.Client.models import tb_client
from django.forms import extras



class ClientForm(forms.ModelForm):
	
	class Meta:
		model = tb_client
		fields = [
		'dni',
		'phoneNumberClient',
		'phoneNumberClientTwo',
		'addressClient',
		'addressClientTwo',
		
		]
		exclude = ['dateCreate', 'user']

		labels = {
		'nameClient':'Nombre Completo de Usuario', 
		'dni':'Numero de su Documento de Identificacion', 
		'phoneNumberClient':'Numero Principal de Contacto',
		'phoneNumberClientTwo': 'Numero Secundario de Contacto',
		'addressClient':'Direccion Principal',
		'addressClientTwo':'Direccion Secundaria',
		
		}
		widgets = {

		'addressClient': Textarea(attrs={'class':'form-control', 
			'required':True ,
			 'autofocus':True,
			  'autocomplete':'off,'
			   ,'placeholder':'Ingrese su direccion principal',
			   'cols': 2, 
			   'rows': 6}),
		'addressClientTwo': Textarea(attrs={'class':'form-control', 
			'required':True , 
			'autofocus':True,
			 'autocomplete':'off',
			  'placeholder':'Ingrese su direccion Secundaria' ,
			  'cols': 2, 
			  'rows': 6}),
		}
          
			