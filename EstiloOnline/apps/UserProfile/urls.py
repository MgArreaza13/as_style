from django.conf.urls import url
from django.contrib import admin
from apps.UserProfile.views import Registro
from apps.UserProfile.views import ListUserProfile
from apps.UserProfile.views import NuevoUsuario
from apps.UserProfile.views import EditUserProfile
from apps.UserProfile.views import DeleteUserProfile
from apps.UserProfile.views import NuevoPerfil

urlpatterns = [
	url(r'^registro/$', Registro, name='Registro'  ),
	url(r'^editar/(?P<id_UserProfile>\d+)$', EditUserProfile, name='EditUserProfile'  ),
	url(r'^borrar/(?P<id_UserProfile>\d+)$', DeleteUserProfile, name='DeleteUserProfile'  ),
	url(r'^nuevousuario/$', NuevoUsuario, name='NuevoUsuario'  ),
	url(r'^nuevoperfil/$', NuevoPerfil, name='NuevoPerfil'  ),
	url(r'^list/$', ListUserProfile , name='List'  ),
  
]