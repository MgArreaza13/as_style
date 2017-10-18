from rest_framework import serializers 
from apps.Service.models import tb_service

class ServiceSerializers (serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_service
		fields = (
			'id',
			'urls',
			'user',
			'nameService',
			'descriptionService',
			'tipoServicio',
			'priceList',
			)