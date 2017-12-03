from django.conf.urls import url
from django.contrib import admin
#Ingresos
from apps.Caja.views import NuevoIngreso
from apps.Caja.views import IngresoList
#Egresos
from apps.Caja.views import NuevoEgreso
from apps.Caja.views import EgresoList
from apps.Caja.views import NuevoPagoReservaOnline
from apps.Caja.views import NuevoPagoTurno


urlpatterns = [

	#url(r'^$', Servicios , name='Servicios'  ),
	#url(r'^Perfil/(?P<id_Client>\d+)$', ClienteProfile , name='ClienteProfile'  ),
	#Ingresos

	url(r'^ajax/nuevo/ingreso/reserva/web/$', NuevoPagoReservaOnline , name='NuevoPagoReservaOnline'  ),
	url(r'^ajax/nuevo/ingreso/turno/web/$', NuevoPagoTurno , name='NuevoPagoTurno'  ),

	url(r'^Ingreso/list/$', IngresoList , name='IngresoList'  ),
	url(r'^Ingreso/Nuevo/$', NuevoIngreso , name='NuevoIngreso'  ),
	

	#Egresos
	url(r'^Egreso/list/$', EgresoList , name='EgresoList'  ),
	url(r'^Egreso/Nuevo/$', NuevoEgreso , name='NuevoEgreso'  ),

	#url(r'^Editar/(?P<id_service>\d+)$', EditService, name='EditService'  ),
	#url(r'^Borrar/(?P<id_service>\d+)$', DeleteService, name='DeleteService'  ),
  
]