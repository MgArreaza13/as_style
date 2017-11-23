from django.db import models
from apps.Configuracion.models import tb_status
from apps.Service.models import tb_service
from apps.Configuracion.models import tb_turn_sesion
from apps.Collaborator.models import tb_collaborator

# Create your models here.
class tb_reservasWeb (models.Model):
	servicioPrestar			= 	models.ForeignKey(tb_service,on_delete=models.CASCADE, null=False, default='')
	collaborator			=	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	dateTurn				=	models.DateField(auto_now=False, auto_now_add=False, null=False, default='' , blank=True)
	turn 					=   models.ForeignKey(tb_turn_sesion, on_delete=models.CASCADE, default='', blank=True)
	mail					=  	models.EmailField(default='', null=False, max_length=30)
	nombre					= 	models.CharField(default='', null=False, max_length=30)
	telefono				=	models.CharField(default='', null=False, max_length=30)
	statusTurn 				=	models.ForeignKey(tb_status, on_delete=models.CASCADE, null=False, default='')
	montoAPagar				=   models.IntegerField(default=0, null=False, blank=True)
	montoPagado				=   models.IntegerField(default=0, null=True, blank=True)
	isPay			 		=	models.BooleanField(null=False, blank=True , default=False)
	description				=	models.TextField(default='Sin Descripcion', null=False, max_length=3000000, blank=True)	
	ingenico_id             =  	models.TextField(default='None', null=False, max_length=3000)
	PagoOnline			 	=	models.BooleanField(null=False, blank=True , default=False)
	def __str__(self):
		return self.mail