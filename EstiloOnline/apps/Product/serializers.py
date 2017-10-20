from rest_framework import serializers 
from apps.Product.models import tb_product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_product
		fields = (
			'user',
			'nameProduct',
			'descriptionProduct',
			'tipoProducto',
			'proveedor',
			'proveedor',
			'priceList',
			'priceCost',
			'alertMinStock',
			'image',
			'dateCreate',
			)