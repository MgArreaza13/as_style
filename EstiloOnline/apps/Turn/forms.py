from django import forms
from django.forms import ModelForm, Textarea ,Select
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.Turn.models import tb_turn
from django.forms import extras



class TurnForm(forms.ModelForm):
	
	class Meta:
		model = tb_turn
		fields = [
		'client',
		'collaborator',
		'servicioPrestar',
		'isPay',
		'statusTurn',
		
		
		
		]
		exclude = ['user', 'dateTurn', 'HoraTurn', 'extraInfoTurn',]

		labels = {
		'dateTurn':'Fecha Para El turno', 
		'isPay':'Es Pagado',
		'statusTurn':'Estatus',
		
		
		}
		widgets = {

		'servicioPrestar': Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione el servicio'}),

		'client':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione el cliente'}),
		
		'collaborator':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione collaborador'}),

		'statusTurn':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione el status'}),
		
		}

  


class NewTurnFormClient(forms.ModelForm):
	
	class Meta:
		model = tb_turn
		fields = [
		'collaborator',
		'servicioPrestar',
		'isPay',
		'statusTurn',
		
		
		
		]
		exclude = ['user', 'client', 'dateTurn', 'HoraTurn', 'extraInfoTurn',]

		labels = {
		'dateTurn':'Fecha Para El turno', 
		'isPay':'Es Pagado',
		'statusTurn':'Estatus',
		
		
		}
		widgets = {

		'servicioPrestar': Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione el servicio'}),

		
		'collaborator':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione collaborador'}),

		'statusTurn':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione el status'}),
		
		}        
		

class EditTurnForm(forms.ModelForm):
	
	class Meta:
		model = tb_turn
		fields = [
		'statusTurn',
		
		
		]
		exclude = ['user', 'dateTurn',  'isPay', 'client', 'collaborator', 'extraInfoTurn',  'servicioPrestar',]

		labels = {
		'statusTurn':'Estatus',
		
		
		}
		widgets = {
		'statusTurn':Select(attrs={'class':'form-control',
			'required':True,
			'autofocus':True,
			'placeholder':'Seleccione el status'}),
		}