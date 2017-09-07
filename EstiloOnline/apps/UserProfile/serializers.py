from rest_framework import serializers
from django.contrib.auth.models import User 
from apps.UserProfile.models import tb_profile

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User 
		fields = ('username',)

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tb_profile
		fields = (
			'user',
			'nameUser',
			'mailUser',
			'birthdayDate',
			'tipoUser',
			'image',
			)