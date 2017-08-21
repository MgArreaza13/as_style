from django.db import models
from django.conf import settings
from apps.Service.models import tb_service
from apps.Proveedores.models import tb_proveedor
from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_formasDePago
from apps.Configuracion.models import tb_tipoEgreso
# Create your models here.

class tb_ingreso (models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	tipoPago				=	models.ForeignKey(tb_formasDePago, on_delete=models.CASCADE, null=False, default='')
	tipoIngreso				=	models.ForeignKey(tb_tipoIngreso, on_delete=models.CASCADE, null=False, default='')
	service					=	models.ForeignKey(tb_service, on_delete=models.CASCADE, null=False, default='')
	monto					=	models.IntegerField(default='', null=False,)
	descripcion	 			=	models.TextField(default='', null=False, max_length=3000)
	#phoneNumberClientTwo	=	models.CharField(default='', null=False, max_length=30)
	#CollaboratorFavoriteKf	= 	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	#addressClientTwo		= 	models.TextField(default='', null=False)
	#isSendPromotions		=	models.BooleanField()
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	#isVip					= 	models.BooleanField()
	#StatusKf				=	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	#TypeClienteKf			=	models.ForeignKey(tb_type_client, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.user.username 


class tb_egreso (models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	tipoPago				=	models.ForeignKey(tb_formasDePago, on_delete=models.CASCADE, null=False, default='')
	proveedor				=	models.ForeignKey(tb_proveedor, on_delete=models.CASCADE, null=False, default='')
	tipoEgreso				= 	models.ForeignKey(tb_tipoEgreso, on_delete=models.CASCADE, null=False, default='')
	monto					=	models.IntegerField(default='', null=False,)
	descripcion	 			=	models.TextField(default='', null=False, max_length=3000)
	#service					=	models.ForeignKey(tb_service, on_delete=models.CASCADE, null=False, default='')
	#phoneNumberClientTwo	=	models.CharField(default='', null=False, max_length=30)
	#CollaboratorFavoriteKf	= 	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	#addressClientTwo		= 	models.TextField(default='', null=False)
	#isSendPromotions		=	models.BooleanField()
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	#isVip					= 	models.BooleanField()
	#StatusKf				=	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	#TypeClienteKf			=	models.ForeignKey(tb_type_client, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.user.username 