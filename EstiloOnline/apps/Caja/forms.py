from django import forms
from django.forms import ModelForm, Textarea, Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso
from django.forms import extras



class IngresoForm(forms.ModelForm):
	
	class Meta:
		model = tb_ingreso
		fields = [
		'tipoPago',
		'tipoIngreso',
		'service',
		'monto',
		
		]
		exclude = ['user', 'dateCreate', 'descripcion',]

		labels = {
		'monto':'Ingrese el monto a pagar', 
		
		}
		widgets = {

		'service':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Servicio'}),

		'tipoPago':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'tipo de Pago'}),

		'tipoIngreso':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'tipo de Pago'}),

		}
          

class EgresoForm(forms.ModelForm):
	
	class Meta:
		model = tb_egreso
		fields = [
		'tipoPago',
		'proveedor',
		'tipoEgreso',
		'monto',
		
		]
		exclude = ['user', 'dateCreate', 'descripcion',]

		labels = {
		'monto':'Ingrese el monto a pagar', 
		
		}
		widgets = {

		'proveedor':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'proveedor'}),

		'tipoPago':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'tipo de Pago'}),

		'tipoEgreso':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'tipo de Egreso'}),
		}
          	