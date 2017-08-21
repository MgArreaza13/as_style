from django.db import models
from django.conf import settings
from apps.Collaborator.models import tb_collaborator
from apps.UserProfile.models import tb_profile
#from apps.Turn.models import tb_status_turn
#from apps.Turn.models 	import tb_turn
# Create your models here.

class tb_type_client(models.Model):
	descriptionType 		=	models.CharField(default='', null=False, max_length=30)

class tb_liquidation_client_header(models.Model):
	codLiquidation			=	models.IntegerField(default='', null=False)
	dateLiquidation			=	models.DateField(auto_now=False, blank=False)
	#idUserExecute			=
	totalAmount				=	models.IntegerField(default='', null=False)
	#turnKf					= 	models.ForeignKey(tb_turn, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.codLiquidation
class tb_invoicer_header_client(models.Model):
	codInvoicer				=	models.IntegerField(default='', null=False)
	dateCreate 				=	models.DateField(auto_now=True, blank=False)
	#idUserExecute
	liquidationClienteKf	=	models.ForeignKey(tb_liquidation_client_header, on_delete=models.CASCADE, null=False, default='')

class tb_client (models.Model):
	user 					=	models.ForeignKey(tb_profile, on_delete=models.CASCADE, null=False, default='')
	dni						=	models.IntegerField(default='', null=False)
	phoneNumberClient		=	models.CharField(default='', null=False, max_length=30)
	phoneNumberClientTwo	=	models.CharField(default='', null=False, max_length=30)
	addressClient 			=	models.TextField(default='', null=False)
	#CollaboratorFavoriteKf	= 	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	#addressClientTwo		= 	models.TextField(default='', null=False)
	#isSendPromotions		=	models.BooleanField()
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	#isVip					= 	models.BooleanField()
	#StatusKf				=	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	#TypeClienteKf			=	models.ForeignKey(tb_type_client, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.user.user.username