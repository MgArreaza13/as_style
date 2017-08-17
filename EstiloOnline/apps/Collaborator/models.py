from django.db import models
from django.conf import settings
from apps.UserProfile.models import tb_profile
from apps.Configuracion.models import tb_tipoCollaborador
from apps.Configuracion.models import tb_tipoComision
# Create your models here.

PAGO_CHOICES = (
    ('Porcentaje', 'Porcentaje por operacion'),
    ('Monto', 'Monto fijo por operacion'),
)

class tb_collaborator(models.Model):
	user 					=	models.ForeignKey(tb_profile, on_delete=models.CASCADE, null=False, default='')
	cuid				    =	models.IntegerField(default='', null=False)
	dni				  		=	models.IntegerField(default='', null=False)
	phoneNumberColl			=	models.CharField(default='', null=False, max_length=30)
	phoneNumberCollTwo		=	models.CharField(default='', null=False, max_length=30)
	addresColl				=	models.TextField(default='', null=False)
	typeCollaborador		=	models.ForeignKey(tb_tipoCollaborador, on_delete=models.CASCADE, null=False, default='')
	Typecomision			=	models.CharField(max_length=30,null=False,choices=PAGO_CHOICES,default='porcentaje',)
	comision				=	models.IntegerField(default='', null=False)
	def __str__(self):
		return self.user.nameUser