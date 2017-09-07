from rest_framework import serializers 

from apps.Turn.models import tb_turn


class turnSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_turn
		fields = ('user',
		'dateTurn',
		'HoraTurn',
		'client',
		'collaborator',
		'extraInfoTurn',
		'servicioPrestar',
		'isProcessClient',
		'isProcessCollaborator',
		'statusTurn',)