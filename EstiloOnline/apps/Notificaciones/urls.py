from django.conf.urls import url
from django.contrib import admin
from apps.Notificaciones.views import NotificacionesView
from apps.Notificaciones.views import NotificacionVista
#from apps.Service.views import Servicios
#from apps.Service.views import NuevoService
#from apps.Service.views import EditService
#from apps.Service.views import DeleteService
#from apps.Service.views import listService


urlpatterns = [

	url(r'^consulta$', NotificacionesView , name='NotificacionesView'  ),
	url(r'^vista/$', NotificacionVista , name='NotificacionVista'  ),
	#url(r'^Perfil/(?P<id_Client>\d+)$', ClienteProfile , name='ClienteProfile'  ),
	#url(r'^list/$', listService , name='listService'  ),
	#url(r'^Nuevo/$', NuevoService , name='NuevoServicio'  ),
	#url(r'^Editar/(?P<id_service>\d+)$', EditService, name='EditService'  ),
	#url(r'^Borrar/(?P<id_service>\d+)$', DeleteService, name='DeleteService'  ),
  
]