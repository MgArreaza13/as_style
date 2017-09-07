from rest_framework import serializers 

from apps.Collaborator.models import tb_collaborator
from apps.Configuracion.models import tb_tipoCollaborador
from apps.UserProfile.models import tb_profile
from django.contrib.auth.models import User 

class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_collaborator
		fields = (
			'url', 
			'user',
			'cuid',
			 'dni', 
			 'phoneNumberColl',
			  'phoneNumberCollTwo',
			   'addresColl', 
			   'Typecomision',
			   'typeCollaborador',
			   'comision',

			   )
