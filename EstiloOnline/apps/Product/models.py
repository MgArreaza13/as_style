from django.db import models
from django.conf import settings
from apps.Client.models import tb_client
from apps.Proveedores.models import tb_proveedor
from apps.Configuracion.models import tb_tipoProducto
#from apps.Turn.models import tb_status_turn
# Create your models here.

class tb_product (models.Model):
	user 				=	 models.ForeignKey(settings.AUTH_USER_MODEL)
	nameProduct			=	 models.CharField(default='', null=False, max_length=30)
	descriptionProduct	=	 models.CharField(default='', null=False, max_length=330)
	tipoProducto 		=	 models.ForeignKey(tb_tipoProducto, on_delete=models.CASCADE, null=False, default='' )
	#codProduct			=	 models.PositiveIntegerField(default='', null=False)
	proveedor			=	 models.ForeignKey(tb_proveedor, on_delete=models.CASCADE, null=False, default='' )
	#addressClient 		=	 models.CharField(default='', null=False, max_length=30)
	#clientProviderKf	=	 models.ForeignKey(tb_client, on_delete=models.CASCADE, null=False, default='')
	#userAdd			=	 models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	priceList			=    models.IntegerField(default='', null=False)
	priceCost			=    models.IntegerField(default='', null=False)
	alertMinStock		=    models.IntegerField(default='', null=False)
	image 				= 	models.ImageField(upload_to='productos/img/', default='', null=False, )
	dateCreate			=	 models.DateField(auto_now=True, blank=False)
	#StatusKf			=	 models.ForeignKey(tb_status_turn, on_delete=models.CASCADE, null=False, default='')
	
	def __str__(self):
		return self.nameProduct
