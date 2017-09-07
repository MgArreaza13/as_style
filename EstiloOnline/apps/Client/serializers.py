from  rest_framework import serializers 

#Modelo 
from apps.Client.models import tb_client 

class ClientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_client
		fields = (
			'user',
			'dni',
			'phoneNumberClient',
			'phoneNumberClientTwo',
			'addressClient',
			)
