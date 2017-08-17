from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import extras

from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_tipoEgreso
from apps.Configuracion.models import tb_tipoServicio
from apps.Configuracion.models import tb_tipoProducto
from apps.Configuracion.models import tb_tipoComision
from apps.Configuracion.models import tb_tipoCollaborador
from apps.Configuracion.models import tb_status
from apps.Configuracion.models import tb_sucursales
from apps.Configuracion.models import tb_formasDePago

class tipoIngresoForm(forms.ModelForm):
	
	class Meta:
		model = tb_tipoIngreso
		fields = [
		'nameTipoIngreso',
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameTipoIngreso':'Ingrese El nombre del Ingreso', 		
		}
		widgets = {
		}


class tipoEgresoForm(forms.ModelForm):
	
	class Meta:
		model = tb_tipoEgreso
		fields = [
		'nameTipoEgreso',
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameTipoEgreso':'Ingrese El nombre del Egreso', 		
		}
		widgets = {
		}


class tipoServicioForm(forms.ModelForm):
	
	class Meta:
		model = tb_tipoServicio
		fields = [
		'nameTipoServicio',
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameTipoServicio':'Ingrese El nombre del Servicio', 		
		}
		widgets = {
		}


class tipoProductoForm(forms.ModelForm):
	
	class Meta:
		model = tb_tipoProducto
		fields = [
		'nameTipoProducto',
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameTipoProducto':'Ingrese El nombre del Producto', 		
		}
		widgets = {
		}
          
class tipoComisionForm(forms.ModelForm):
	
	class Meta:
		model = tb_tipoComision
		fields = [
		'nameTipoComision',
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameTipoComision':'Ingrese El monto de la Comision', 		
		}
		widgets = {
		}

class tipoCollaboradorForm(forms.ModelForm):
	
	class Meta:
		model = tb_tipoCollaborador
		fields = [
		'nameTipoCollaborador',
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameTipoCollaborador':'Ingrese El tipo del Collaborador', 		
		}
		widgets = {
		}
          

class tipoStatusForm(forms.ModelForm):
	
	class Meta:
		model = tb_status
		fields = [
		'nameStatus',
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameStatus':'Ingrese El status', 		
		}
		widgets = {
		}


class sucursalesForm(forms.ModelForm):
	
	class Meta:
		model = tb_sucursales
		fields = [
		'nameSucursales',
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameSucursales':'Ingrese El nombre de la sucursal', 		
		}
		widgets = {
		}

class formasDePagoForm(forms.ModelForm):
	
	class Meta:
		model = tb_formasDePago
		fields = [
		'nameFormasDePago',
		]
		exclude = ['user','dateCreate']

		labels = {
		'nameFormasDePago':'Ingrese El metodo de pago que desea agregar', 		
		}
		widgets = {
		}