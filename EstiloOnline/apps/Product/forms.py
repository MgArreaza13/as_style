from django import forms
from django.forms import ModelForm, Textarea , Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.Product.models import tb_product
from django.forms import extras



class ProductForm(forms.ModelForm):
	
	class Meta:
		model = tb_product
		fields = [
		'nameProduct',
		'descriptionProduct',
		'tipoProducto',
		'codProduct',
		'proveedor',
		'priceList',
		'priceCost',
		'alertMinStock',
		'urlPhoto',
		
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameProduct':'Ingrese El nombre del Producto',
		'descriptionProduct':'Ingrese la Descripcion del Producto',
		'codProduct':'Ingrese El codigo Del Producto',
		'proveedor':'Seleccione al Proveedor del producto',
		'priceList':'Precio para vender',
		'priceCost':'Precio de costo del producto',
		'alertMinStock':'Ingrese el monto que desea que le avise el stock',
		'urlPhoto':'Ingrese la url de la foto del producto',
		
		}
		widgets = {

		'descriptionProduct': Textarea(attrs={'class':'form-control', 
			'required':True ,
			 'autofocus':True,
			  'autocomplete':'off,'
			   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
			   'cols': 2, 
			   'rows': 6}),
		
		'proveedor':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Proveedor'}),

		'tipoProducto':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Proveedor'}),
		
		}
          
			