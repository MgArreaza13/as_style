from rest_framework import serializers
from django.contrib.auth.models import User 
from apps.UserProfile.models import tb_profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User 
		fields = ('id','url','username','password')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	user_id = serializers.ReadOnlyField(source='user.id')
	class Meta:
		model = tb_profile
		fields = (
			'id',
			'url',
			'user_id',
			'user',
			'nameUser',
			'mailUser',
			'birthdayDate',
			'tipoUser',
			'image',
			)