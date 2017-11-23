from rest_framework import serializers
from apps.ReservasWeb.models import tb_reservasWeb


class ReservasWebSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_reservasWeb
		fields = (
			'dateTurn',
			'HoraTurn',
			'mail',
			'nombre',
			'telefono',
			'statusTurn',
			)