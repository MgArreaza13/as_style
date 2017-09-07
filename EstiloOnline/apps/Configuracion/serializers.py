#rest 
from rest_framework import serializers 

#Modelos 
from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_tipoEgreso
from apps.Configuracion.models import tb_tipoServicio
from apps.Configuracion.models import tb_tipoProducto
from apps.Configuracion.models import tb_tipoComision
from apps.Configuracion.models import tb_tipoCollaborador
from apps.Configuracion.models import tb_status
from apps.Configuracion.models import tb_sucursales
from apps.Configuracion.models import tb_formasDePago


class TipoIngresoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoIngreso
		fields = ('user', 'nameTipoIngreso', 'dateCreate')

class TipoEgresoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoEgreso
		fields = ('user', 'nameTipoEgreso', 'dateCreate')

class TipoServicioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoServicio
		fields = ('user', 'nameTipoServicio', 'dateCreate')

class TipoProductoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoProducto
		fields = ('user', 'nameTipoProducto', 'dateCreate')

class TipoComisionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoComision
		fields = ('user', 'nameTipoComision', 'dateCreate')

class TipoColaboradorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoCollaborador
		fields = ('user', 'nameTipoCollaborador', 'dateCreate')

class StatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_status
		fields = ('user', 'nameStatus', 'dateCreate')

class SucursalesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_sucursales
		fields = ('user', 'nameSucursales', 'dateCreate')


class FormasDePagoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_formasDePago
		fields = ('user', 'nameFormasDePago', 'dateCreate')