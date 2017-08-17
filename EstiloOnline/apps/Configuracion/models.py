from django.db import models
from django.conf import settings
# Create your models here.


class tb_tipoIngreso(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameTipoIngreso			=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameTipoIngreso


class tb_tipoEgreso(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameTipoEgreso			=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameTipoEgreso

class tb_tipoServicio(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameTipoServicio		=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameTipoServicio


class tb_tipoProducto(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameTipoProducto		=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameTipoProducto

class tb_tipoComision(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameTipoComision		=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameTipoComision


class tb_tipoCollaborador(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameTipoCollaborador	=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameTipoCollaborador

class tb_status(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameStatus				=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameStatus	


class tb_sucursales(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameSucursales			=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameSucursales	


class tb_formasDePago(models.Model):
	user 					=	models.ForeignKey(settings.AUTH_USER_MODEL)
	nameFormasDePago		=	models.CharField(default='', null=False, max_length=30, unique=True)
	dateCreate				=	models.DateField(auto_now=True, blank=False)
	def __str__(self):
		return self.nameFormasDePago	