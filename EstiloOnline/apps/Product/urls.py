from django.conf.urls import url
from django.contrib import admin
#from apps.Proveedores.views import Servicios
from apps.Product.views import NuevoProducto
from apps.Product.views import EditarProducto
from apps.Product.views import EliminarProducto
from apps.Product.views import ListProductos
from apps.Product.views import pructosCliente
from apps.Product.views import ProductiDetail


urlpatterns = [

	#url(r'^$', Servicios , name='Servicios'  ),
	#url(r'^Perfil/(?P<id_Client>\d+)$', ClienteProfile , name='ClienteProfile'  ),
	url(r'^list/$', ListProductos , name='ListProductos'  ),
	url(r'^detalles/$', pructosCliente , name='pructosCliente'  ),
	url(r'^Nuevo/$', NuevoProducto , name='NuevoProducto'  ),
	url(r'^Editar/(?P<id_producto>\d+)$', EditarProducto, name='EditarProducto'  ),
	url(r'^Borrar/(?P<id_producto>\d+)$', EliminarProducto, name='EliminarProducto'  ),
  	url(r'^consulta/detail$', ProductiDetail, name='ProductiDetail'  ),
]