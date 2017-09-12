from django.conf.urls import url
from django.contrib import admin
#Ingresos
from apps.Caja.views import NuevoIngreso
from apps.Caja.views import NuevoIngresoTurn
from apps.Caja.views import IngresoList
from apps.Caja.views import IngresoTurnList
#Egresos
from apps.Caja.views import NuevoEgreso
from apps.Caja.views import EgresoList

urlpatterns = [

	#url(r'^$', Servicios , name='Servicios'  ),
	#url(r'^Perfil/(?P<id_Client>\d+)$', ClienteProfile , name='ClienteProfile'  ),
	#Ingresos
	url(r'^Ingreso/list/$', IngresoList , name='IngresoList'  ),
	url(r'^Ingreso/list/turnos$', IngresoTurnList , name='IngresoTurnList'  ),
	url(r'^Ingreso/Nuevo/$', NuevoIngreso , name='NuevoIngreso'  ),
	url(r'^Ingreso/Nuevo/turno/(?P<id_turn>\d+)$', NuevoIngresoTurn , name='NuevoIngresoTurn'  ),

	#Egresos
	url(r'^Egreso/list/$', EgresoList , name='EgresoList'  ),
	url(r'^Egreso/Nuevo/$', NuevoEgreso , name='NuevoEgreso'  ),

	#url(r'^Editar/(?P<id_service>\d+)$', EditService, name='EditService'  ),
	#url(r'^Borrar/(?P<id_service>\d+)$', DeleteService, name='DeleteService'  ),
  
]