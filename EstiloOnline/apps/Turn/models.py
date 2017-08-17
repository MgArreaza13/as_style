from django.db import models
from django.conf import settings
from apps.Client.models import tb_client
from apps.Collaborator.models import tb_collaborator
from apps.Product.models import tb_product
from apps.Service.models import tb_service
from apps.Configuracion.models import tb_status
# Create your models here.

"""
class tb_status_turn (models.Model):
	nameTurnStatus			=	models.CharField(default='', null=False, max_length=30)
	def __str__(self):
		return self.nameTurnStatus


class tb_tipe_detail (models.Model):
	descriptionDetail		=	models.CharField(default='', null=False, max_length=30)
	def __str__(self):
		return self.descriptionDetail


class tb_turn_session_detail (models.Model):
	TurnKf					= 	models.ForeignKey(tb_turn , on_delete=models.CASCADE, null=False, default='')
	dateAdd					=	models.DateField(auto_now=False, auto_now_add=False, blank=False)
	TipeDetailKf			=	models.ForeignKey(tb_tipe_detail , on_delete=models.CASCADE, null=False, default='')
	priceDetail				=	models.IntegerField(default='', null=False)
	#idUserAdd				=	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ProductKf				=	models.ForeignKey(tb_product, on_delete=models.CASCADE, null=False, default='')
	ServiceKf				=	models.ForeignKey(tb_service, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.dateAdd


"""

TURNO_CHOICES = (
    ('Mañana', 'Desea un turno en la Mañana'),
    ('Tarde', 'Desea Un Turno En la Tarde'),
)
class tb_turn (models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	#codTurn					=	models.IntegerField(default='', null=False)
	dateTurn				=	models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False, default='')
	#TypeHora				=	models.CharField(max_length=30,null=False,choices=TURNO_CHOICES,default='Mañana',)
	HoraTurn				=	models.TimeField(auto_now=False, auto_now_add=False, blank=False, null=False, default='')
	client					=  	models.ForeignKey(tb_client, on_delete=models.CASCADE, null=False, default='')
	collaborator			=	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	extraInfoTurn			=	models.TextField(default='', null=False, max_length=300)
	servicioPrestar			= 	models.ForeignKey(tb_service,on_delete=models.CASCADE, null=False, default='')
	isProcessClient 		=	models.BooleanField()
	isProcessCollaborator 	=	models.BooleanField()
	statusTurn 				=	models.ForeignKey(tb_status, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.client.user.nameUser