from apps.Notificaciones.models import Notificacion 
#rest 
from rest_framework import serializers 

class NotiticacionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Notificacion
		fields = ('url','id','nombre', 'dateTurn', 'HoraTurn', 'leida')