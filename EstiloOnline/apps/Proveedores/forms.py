from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.Proveedores.models import tb_proveedor
from django.forms import extras



class ProveedorForm(forms.ModelForm):
	
	class Meta:
		model = tb_proveedor
		fields = [
		'razonSocial',
		'cuit',
		'nameProveedor',
		'email',
		'personaACargo',
		'paginaWeb',
		'urlPhoto',
		'phoneNumberProveedor',
		'phoneNumberProveedorTwo',
		'addressProveedor',
		'addressProveedorTwo',
		
		]
		exclude = ['user','dateCreate']

		labels = {
		'razonSocial':'Razon Social Del Nuevo Proveedor', 
		'cuit':'Cuit del nuevo proveedor', 
		'nameProveedor':'Ingrese el nombre del proveedor',
		'email':'Ingrese el Correo de contacto del proveedor',
		'personaACargo': 'Ingrese el nombre de la persona a cargo',
		'paginaWeb':'Pagina web del proveedor',
		'urlPhoto': 'url del Logo del proveedor',
		'phoneNumberProveedor':'Numero de Telefono Primario',
		'phoneNumberProveedorTwo': 'Numero de Telefono Primario Secundario',
		
		}
		widgets = {

		'addressProveedor': Textarea(attrs={'class':'form-control', 
			'required':True ,
			 'autofocus':True,
			  'autocomplete':'off,'
			   ,'placeholder':'Direccion Principal Del Nuevo Proveedor',
			   'cols': 2, 
			   'rows': 6}),
		
		'addressProveedorTwo': Textarea(attrs={'class':'form-control', 
			'required':True ,
			 'autofocus':True,
			  'autocomplete':'off,'
			   ,'placeholder':'Direccion Secundaria Del Nuevo Proveedor',
			   'cols': 2, 
			   'rows': 6}),
		}
          
			