from django.db import models
from django.conf import settings
#from apps.Turn.models import tb_status_turn

# Create your models here.


class tb_profile (models.Model):
	user			=	models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, default='')
	nameUser		=	models.CharField(default='', null=False, max_length=30)
	mailUser		=	models.EmailField(default='', null=False, max_length=30)
	birthdayDate	=	models.DateField(auto_now=False, auto_now_add=False, blank=False )
	#image 			= 	models.ImageField(upload_to='users/avatar/', default='', null=False, )
	tipoUser		=   models.CharField(default='', null=False, max_length=30) # Esto se utilizara para saber si es admin, colaborador o client
	image 			= 	models.ImageField(upload_to='users/avatar/', default='', null=False, )
	#nameProfile	=	models.CharField(default='', null=False, max_length=30)
	#StatusKf		= 	models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	def __str__(self):
		return self.nameUser
