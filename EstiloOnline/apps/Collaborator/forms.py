from django import forms
from django.forms import ModelForm, Textarea , Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.Collaborator.models import tb_collaborator
from django.forms import extras



class ColaboradorForm(forms.ModelForm):
	
	class Meta:
		model = tb_collaborator
		fields = [
		'cuid',
		'dni',
		'phoneNumberColl',
		'phoneNumberCollTwo',
		'addresColl',

		'typeCollaborador',
		'Typecomision',
		'comision',
		
		]
		exclude = ['user',]

		labels = {
		'cuid':'Numero de CUIT',  
		'dni':'Numero de su Documento de Identificacion', 
		'phoneNumberColl':'Numero particular de Contacto',
		'phoneNumberCollTwo': 'Numero movil de Contacto',
		'addresColl':'Direccion Principal',
		'Typecomision':'Ingrese el tipo de comision',
		'typeCollaborador':'Cual Es la profesion del Colaborador',
		'comision':'Comision que se le otorgara al Colaborador'
		
		}
		widgets = {

		'addresColl': Textarea(attrs={'class':'form-control', 
			'required':True ,
			 'autofocus':True,
			  'autocomplete':'off,'
			   ,'placeholder':'Ingrese su direccion principal',
			   'cols': 2, 
			   'rows': 6}),
		'typeCollaborador':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione el tipo de collaborador'}),

		'Typecomision':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione la comision del collaborador'}),
		}
          
			