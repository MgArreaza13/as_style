from django.db import models
from django.conf import settings

# Create your models here.


class tb_proveedor (models.Model):
	user 						=	models.ForeignKey(settings.AUTH_USER_MODEL)
	razonSocial					=	models.CharField(default='', null=False, max_length=30)
	cuit						=	models.IntegerField(default='', null=False)
	nameProveedor				=	models.CharField(default='', null=False, max_length=30)
	phoneNumberProveedor		=	models.CharField(default='', null=False, max_length=30)
	phoneNumberProveedorTwo		=	models.CharField(default='', null=False, max_length=30)
	addressProveedor 			=	models.TextField(default='', null=False)
	email 						= 	models.EmailField(default='', null=False, max_length=30)
	personaACargo				=	models.CharField(default='', null=False, max_length=30)
	paginaWeb 					=	models.URLField(default='', null=False,max_length=3000)
	urlPhoto					=   models.URLField(default='', null=False,max_length=3000)
	#CollaboratorFavoriteKf		= 	models.ForeignKey(tb_collaborator, on_delete=models.CASCADE, null=False, default='')
	addressProveedorTwo			= 	models.TextField(default='', null=False)
	#isSendPromotions			=	models.BooleanField()
	dateCreate					=	models.DateField(auto_now=True, blank=False)
	#isVip						= 	models.BooleanField()
	#StatusKf					=	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	#TypeClienteKf				=	models.ForeignKey(tb_type_client, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.nameProveedor