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
from apps.Configuracion.models import tb_turn_sesion

class TipoIngresoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoIngreso
		fields = ('id',
			'url','user', 'nameTipoIngreso', 'dateCreate')

class TipoEgresoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoEgreso
		fields = ('id',
			'url','user', 'nameTipoEgreso', 'dateCreate')

class TipoServicioSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoServicio
		fields = ('id',
			'url','user', 'nameTipoServicio', 'dateCreate')

class TipoProductoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoProducto
		fields = ('id',
			'url','user', 'nameTipoProducto', 'dateCreate')

class TipoComisionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoComision
		fields = ('id',
			'url','user', 'nameTipoComision', 'dateCreate')

class TipoColaboradorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_tipoCollaborador
		fields = ('id',
			'url','user', 'nameTipoCollaborador', 'dateCreate')

class StatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_status
		fields = ('id',
			'url','user', 'nameStatus', 'dateCreate')

class SucursalesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_sucursales
		fields = ('id',
			'url','user', 'nameSucursales', 'dateCreate')


class FormasDePagoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_formasDePago
		fields = ('id',
			'url','user', 'nameFormasDePago', 'dateCreate')


class TurnSesionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_turn_sesion
		fields = ('id',
			'url','user', 'nameturnsession', 'HoraTurn','HoraTurnEnd',)