from django.db import models

# Create your models here.


class Notificacion(models.Model):
	#servicioPrestar			= 	models.ForeignKey(tb_service,on_delete=models.CASCADE, null=False, default='')
	dateTurn				=	models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False, default='')
	HoraTurn				=	models.DateField(auto_now=True, blank=False)
	#mail					=  	models.EmailField(default='', null=False, max_length=30)
	nombre					= 	models.CharField(default='', null=False, max_length=30)
	#telefono				=	models.CharField(default='', null=False, max_length=30)
	#statusTurn 				=	models.ForeignKey(tb_status, on_delete=models.CASCADE, null=False, default='')
	#montoAPagar				=   models.IntegerField(default=0, null=False, blank=True)
	#description				=	models.CharField(default='Sin Descripcion', null=False, max_length=30, blank=True)	
	leida				 	=	models.BooleanField(default=False)
	def __str__(self):
		return self.nombre