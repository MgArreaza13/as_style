from rest_framework import serializers
from apps.ReservasWeb.models import tb_reservasWeb


class ReservasWebSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_reservasWeb
		fields = (
			'id',
			'url',
			'servicioPrestar',
			'collaborator',
			'dateTurn',
			'turn',
			'mail',
			'nombre',
			'telefono',
			'statusTurn',
			'montoAPagar',
			'montoPagado',
			'isPay',
			'description',
			'ingenico_id',
			'PagoOnline',
			)