from django import forms
from django.forms import ModelForm, Textarea, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.Service.models import tb_service
from django.forms import extras



class ServiceForm(forms.ModelForm):
	
	class Meta:
		model = tb_service
		fields = [
		'nameService',
		'descriptionService',
		'tipoServicio',
		'codService',
		'priceList',
		
		]
		exclude = ['user',]

		labels = {
		'nameService':'Nombre del Servicio a prestar', 
		'descriptionService':'Descripcion del Servicio a prestar', 
		'codService':'codigo del servicio',
		'priceList': 'Precio para vender el servicio',
		
		}
		widgets = {

		'descriptionService': Textarea(attrs={'class':'form-control', 
			'required':True ,
			 'autofocus':True,
			  'autocomplete':'off,'
			   ,'placeholder':'Ingrese la descripcion para vender el servicio',
			   'cols': 2, 
			   'rows': 6}),
		
		'tipoServicio':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Proveedor'}),
		}
          
			