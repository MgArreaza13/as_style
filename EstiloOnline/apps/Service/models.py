from django.db import models
from django.conf import settings
from apps.Client.models import tb_client
from apps.Configuracion.models import tb_tipoServicio
#from apps.Turn.models import tb_status_turn
# Create your models here.

class tb_service(models.Model):
	user 				=	 models.ForeignKey(settings.AUTH_USER_MODEL)
	nameService			=	 models.CharField(default='', null=False, max_length=30)
	descriptionService	=	 models.TextField(default='', null=False)
	tipoServicio		=	 models.ForeignKey(tb_tipoServicio, on_delete=models.CASCADE, null=False, default='')
	codService			=	 models.PositiveIntegerField(default='', null=False)
	#addressClient 		=	 models.CharField(default='', null=False, max_length=30)
	#clientProviderKf	=	 models.ForeignKey(tb_client, on_delete=models.CASCADE, null=False, default='')
	#iduserAdd			=	 models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	priceList			=    models.IntegerField(default='', null=False)
	#urlPhoto			=    models.URLField(max_length=300)
	#StatusKf			=	 models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	
	def __str__(self):
		return self.nameService