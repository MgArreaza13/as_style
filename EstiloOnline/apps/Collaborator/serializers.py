from rest_framework import serializers 

from apps.Collaborator.models import tb_collaborator

class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_collaborator
		fields = ('url', 'cuid', 'dni', 'phoneNumberColl', 'phoneNumberCollTwo', 'addresColl', )
