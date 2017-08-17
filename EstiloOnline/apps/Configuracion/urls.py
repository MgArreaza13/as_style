from django.conf.urls import url
from django.contrib import admin
from apps.Configuracion.views import Configuracion
#ingresos
from apps.Configuracion.views import NuevoTipoIngreso
from apps.Configuracion.views import EditarTipoIngreso
from apps.Configuracion.views import BorrarTipoIngreso
#egresos
from apps.Configuracion.views import NuevoTipoEgreso
from apps.Configuracion.views import EditarTipoEgreso
from apps.Configuracion.views import BorrarTipoEgreso
#status
from apps.Configuracion.views import NuevoStatus
from apps.Configuracion.views import EditarStatus
from apps.Configuracion.views import BorrarStatus
#Collaboradores
from apps.Configuracion.views import NuevoTipoCollaborador
from apps.Configuracion.views import EditarTipoCollaborador
from apps.Configuracion.views import BorrarTipoCollaborador
#servicios
from apps.Configuracion.views import NuevoTipoServicio
from apps.Configuracion.views import EditarTipoServicio
from apps.Configuracion.views import BorrarTipoServicio
#productos
from apps.Configuracion.views import NuevoTipoProducto
from apps.Configuracion.views import EditarTipoProducto
from apps.Configuracion.views import BorrarTipoProducto
#comision
from apps.Configuracion.views import NuevoTipoComision
from apps.Configuracion.views import EditarTipoComision
from apps.Configuracion.views import BorrarTipoComision

#sucursales

from apps.Configuracion.views import nuevaSucursal
from apps.Configuracion.views import EditarSucursal
from apps.Configuracion.views import BorrarSucursal

#FormasDePago

from apps.Configuracion.views import nuevaFormaDePago
from apps.Configuracion.views import EditarFormaDePago
from apps.Configuracion.views import BorrarFormaDePago



urlpatterns = [

	url(r'^$', Configuracion , name='Configuracion'  ),
	#ingresos
	url(r'^TipoIngreso/Nuevo/$', NuevoTipoIngreso , name='NuevoTipoIngreso'  ),
	url(r'^TipoIngreso/Editar/(?P<id_tipoIngreso>\d+)$', EditarTipoIngreso, name='EditarTipoIngreso'  ),
	url(r'^TipoIngreso/Borrar/(?P<id_tipoIngreso>\d+)$', BorrarTipoIngreso, name='BorrarTipoIngreso'  ),
	#egresos
	url(r'^TipoEgreso/Nuevo/$', NuevoTipoEgreso , name='NuevoTipoEgreso'  ),
	url(r'^TipoEgreso/Editar/(?P<id_tipoEgreso>\d+)$', EditarTipoEgreso, name='EditarTipoEgreso'  ),
	url(r'^TipoEgreso/Borrar/(?P<id_tipoEgreso>\d+)$', BorrarTipoEgreso, name='BorrarTipoEgreso'  ),
	#Status
	url(r'^Status/Nuevo/$', NuevoStatus , name='NuevoStatus'  ),
	url(r'^Status/Editar/(?P<id_status>\d+)$', EditarStatus, name='EditarStatus'  ),
	url(r'^Status/Borrar/(?P<id_status>\d+)$', BorrarStatus, name='BorrarStatus'  ),
	#Collaboradores
	url(r'^TipoCollaboradores/Nuevo/$', NuevoTipoCollaborador , name='NuevoTipoCollaborador'  ),
	url(r'^TipoCollaboradores/Editar/(?P<id_TipoCollaborador>\d+)$', EditarTipoCollaborador, name='EditarTipoCollaborador'  ),
	url(r'^TipoCollaboradores/Borrar/(?P<id_TipoCollaborador>\d+)$', BorrarTipoCollaborador, name='BorrarTipoCollaborador'  ),
	#Servicios
	url(r'^TipoServicio/Nuevo/$', NuevoTipoServicio , name='NuevoTipoServicio'  ),
	url(r'^TipoServicio/Editar/(?P<id_TipoServicio>\d+)$', EditarTipoServicio, name='EditarTipoServicio'  ),
	url(r'^TipoServicio/Borrar/(?P<id_TipoServicio>\d+)$', BorrarTipoServicio, name='BorrarTipoServicio'  ),
	#Productos
	url(r'^TipoProducto/Nuevo/$', NuevoTipoProducto , name='NuevoTipoProducto'  ),
	url(r'^TipoProducto/Editar/(?P<id_TipoProducto>\d+)$', EditarTipoProducto, name='EditarTipoProducto'  ),
	url(r'^TipoProducto/Borrar/(?P<id_TipoProducto>\d+)$', BorrarTipoProducto, name='BorrarTipoProducto'  ),
	#Comision
	url(r'^TipoComision/Nuevo/$', NuevoTipoComision , name='NuevoTipoComision'  ),
	url(r'^TipoComision/Editar/(?P<id_TipoComision>\d+)$', EditarTipoComision, name='EditarTipoComision'  ),
	url(r'^TipoComision/Borrar/(?P<id_TipoComision>\d+)$', BorrarTipoComision, name='BorrarTipoComision'  ),
	#Sucursal
	url(r'^Sucursal/Nuevo/$', nuevaSucursal , name='nuevaSucursal'  ),
	url(r'^Sucursal/Editar/(?P<id_Sucursal>\d+)$', EditarSucursal, name='EditarSucursal'  ),
	url(r'^Sucursal/Borrar/(?P<id_Sucursal>\d+)$', BorrarSucursal, name='BorrarSucursal'  ),
	#FormaDePago
	url(r'^FormaDePago/Nuevo/$', nuevaFormaDePago , name='nuevaFormaDePago'  ),
	url(r'^FormaDePago/Editar/(?P<id_FormaDePago>\d+)$', EditarFormaDePago, name='EditarFormaDePago'  ),
	url(r'^FormaDePago/Borrar/(?P<id_FormaDePago>\d+)$', BorrarFormaDePago, name='BorrarFormaDePago'  ),



	#url(r'^Perfil/(?P<id_Client>\d+)$', ClienteProfile , name='ClienteProfile'  ),
	#url(r'^list/$', ListProductos , name='ListProductos'  ),
 
]