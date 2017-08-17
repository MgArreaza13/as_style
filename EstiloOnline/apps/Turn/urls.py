from django.conf.urls import url
from django.contrib import admin
from apps.Turn.views import listTurnos
from apps.Turn.views import NuevoTurn
from apps.Turn.views import NuevoTurnParaHoy
from apps.Turn.views import EditTurnStatus
from apps.Turn.views import EditTurn
from apps.Turn.views import DeleteTurn
from apps.Turn.views import index
from apps.Turn.views import EditTurnList


urlpatterns = [

	url(r'^$', index , name='index'  ),
	#url(r'^Perfil/(?P<id_Client>\d+)$', ClienteProfile , name='ClienteProfile'  ),
	url(r'^list/$', listTurnos , name='listTurnos'  ),
	url(r'^list/Status/(?P<id_turn>\d+)$', EditTurnList , name='EditTurnList'  ),
	url(r'^Nuevo/Hoy$', NuevoTurnParaHoy , name='NuevoTurnParaHoy'  ),
	url(r'^Nuevo/$', NuevoTurn , name='NuevoTurn'  ),
	url(r'^Actualizar/Status/(?P<id_turn>\d+)$', EditTurnStatus, name='EditTurnStatus'  ),
	url(r'^Editar/(?P<id_turn>\d+)$', EditTurn, name='EditTurn'  ),
	url(r'^Borrar/(?P<id_turn>\d+)$', DeleteTurn, name='DeleteTurn'  ),
  
]