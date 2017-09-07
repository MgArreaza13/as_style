from rest_framework import serializers

from apps.Proveedores.models import tb_proveedor


class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_proveedor
		fields = (
				'user',
				'razonSocial',
				'cuit',
				'nameProveedor',
				'phoneNumberProveedor',
				'phoneNumberProveedorTwo',
				'addressProveedor',
				'email',
				'personaACargo',
				'paginaWeb',
				'urlPhoto',
				'dateCreate',
				)
