from django.conf.urls import url
from django.contrib import admin
from apps.Client.views import Clientes 
from apps.Client.views import list
from apps.Client.views import NuevoClient 
from apps.Client.views import EditClient
from apps.Client.views import DeleteClient 
from apps.Client.views import ClienteProfile
from apps.Client.views import CitasPedidasClient
from apps.Client.views import CitasAtendidasClient
from apps.Client.views import CitasEnProcesoClient
from apps.Client.views import CitasEnEsperaClient
from apps.Client.views import CitasCanceladasClient
from apps.Client.views import HistorialCitasClient
from apps.Client.views import NuevoClientProfile

urlpatterns = [

	url(r'^$', Clientes , name='ClientesHome'  ),
	url(r'^Perfil/(?P<id_Client>\d+)$', ClienteProfile , name='ClienteProfile'  ),
	url(r'^CitasPedidas/(?P<id_Client>\d+)$', CitasPedidasClient , name='CitasPedidasClient'  ),
	url(r'^CitasAtendidas/(?P<id_Client>\d+)$', CitasAtendidasClient , name='CitasAtendidasClient'  ),
	url(r'^CitasEnProceso/(?P<id_Client>\d+)$', CitasEnProcesoClient , name='CitasEnProcesoClient'  ),
	url(r'^CitasEnEspera/(?P<id_Client>\d+)$', CitasEnEsperaClient , name='CitasEnEsperaClient'  ),
	url(r'^CitasCanceladas/(?P<id_Client>\d+)$', CitasCanceladasClient , name='CitasCanceladasClient'  ),
	url(r'^HistorialCliente/(?P<id_Client>\d+)$', HistorialCitasClient , name='HistorialCitasClient'  ),
	url(r'^list/$', list , name='list'  ),
	url(r'^Nuevo/$', NuevoClient , name='NuevoCliente'  ),
	url(r'^NuevoProfile/$', NuevoClientProfile , name='NuevoClientProfile'  ),
	url(r'^Editar/(?P<id_Client>\d+)$', EditClient, name='EditClient'  ),
	url(r'^Borrar/(?P<id_Client>\d+)$', DeleteClient, name='DeleteClient'  ),
  
]