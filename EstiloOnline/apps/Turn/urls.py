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
from apps.Turn.views import NuevoTurnClient
from apps.Turn.views import turno_update
from apps.Turn.views import InfoReserva
from apps.Turn.views import InfoTurno
from apps.Turn.views import ActualizacionManualTurno

urlpatterns = [

	url(r'^$', index , name='index'  ),
	#url(r'^Perfil/(?P<id_Client>\d+)$', ClienteProfile , name='ClienteProfile'  ),
	url(r'^list/$', listTurnos , name='listTurnos'  ),
	url(r'^list/Status/(?P<id_turn>\d+)$', EditTurnList , name='EditTurnList'  ),
	url(r'^Nuevo/Hoy$', NuevoTurnParaHoy , name='NuevoTurnParaHoy'  ),
	url(r'^Nuevo/$', NuevoTurn , name='NuevoTurn'  ),
	url(r'^Nuevo/(?P<id_client>\d+)$', NuevoTurnClient , name='NuevoTurnClient'  ),
	url(r'^Actualizar/Status/(?P<id_turn>\d+)$', EditTurnStatus, name='EditTurnStatus'  ),
	url(r'^Editar/(?P<id_turn>\d+)$', EditTurn, name='EditTurn'  ),
	url(r'^Borrar/(?P<id_turn>\d+)$', DeleteTurn, name='DeleteTurn'  ),
  	url(r'^actualizacion/de/status$', turno_update , name='turno_update'  ),
  	url(r'^info/de/reservas$', InfoReserva , name='InfoReserva'  ),
	url(r'^info/de/turno$', InfoTurno , name='InfoTurno'  ),
	url(r'^cambiar/de/turno$', ActualizacionManualTurno , name='ActualizacionManualTurno'  ),
]