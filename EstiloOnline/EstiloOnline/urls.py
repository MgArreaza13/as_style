"""EstiloOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import refresh_jwt_token
#rest framework
from rest_framework import routers
router =  routers.DefaultRouter()

#modulos 

###################CLIENT###########################
from apps.Client.views import ClienteViewset
router.register(r'api/clientes', ClienteViewset)
##################COLABORADORES######################
from apps.Collaborator.views import CollaboratorViewset
router.register(r'api/colaboradores', CollaboratorViewset)
##################CONFIGURACION######################
from apps.Configuracion.views import TipoIngresoViewset
from apps.Configuracion.views import TipoEgresoViewset
from apps.Configuracion.views import TipoServicioViewset
from apps.Configuracion.views import TipoProductoViewset
from apps.Configuracion.views import TipoComisionViewset
from apps.Configuracion.views import TipoColaboradorViewset
from apps.Configuracion.views import StatusViewset
from apps.Configuracion.views import SucursalesViewset
from apps.Configuracion.views import FormasDePagoViewset
from apps.ReservasWeb.views import ReservasWebViewsets
from apps.Configuracion.views import TurnSesionViewset
router.register(r'api/tipoingreso', TipoIngresoViewset)
router.register(r'api/tipoegreso', TipoEgresoViewset)
router.register(r'api/tiposervicio', TipoServicioViewset)
router.register(r'api/tipoproducto', TipoProductoViewset)
router.register(r'api/tipocomision', TipoComisionViewset)
router.register(r'api/tipocolaborador', TipoColaboradorViewset)
router.register(r'api/status', StatusViewset)
router.register(r'api/sucursales', SucursalesViewset)
router.register(r'api/fromasdepago', FormasDePagoViewset)
router.register(r'api/reservas/web', ReservasWebViewsets)
router.register(r'api/sesiones', TurnSesionViewset)
################PRODUCTOS############################
from apps.Product.views import ProductViewset
router.register(r'api/productos', ProductViewset)

################PROVEEDORES##########################
from apps.Proveedores.views import ProveedoresViewset
router.register(r'api/proveedores', ProveedoresViewset)

################SERVICE#############################
from apps.Service.views import ServicioViewset
router.register(r'api/servicios', ServicioViewset)

###############TURNOS##############################
from apps.Turn.views import TurnViewsets
router.register(r'api/turnos', TurnViewsets)


##############USERPROFILE##################################
from apps.UserProfile.views import UserViewset 
from apps.UserProfile.views import UserProfileViewset
router.register(r'api/usuarios', UserViewset)
router.register(r'api/perfiles', UserProfileViewset)


############NOTIFICACIONE############
from apps.Notificaciones.views import NotificacionViewsets

router.register(r'api/notificaciones', NotificacionViewsets)



urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^', include('apps.PanelPrincipal.urls', namespace='Panel')),
    url(r'^usuarios/', include('apps.UserProfile.urls', namespace='Usuarios')),
    url(r'^clientes/', include('apps.Client.urls', namespace='Clientes')),
    url(r'^servicios/', include('apps.Service.urls', namespace='Servicios')),
    url(r'^productos/', include('apps.Product.urls', namespace='Productos')),
    url(r'^colaboradores/', include('apps.Collaborator.urls', namespace='Colaboradores')),
    url(r'^proveedores/', include('apps.Proveedores.urls', namespace='Proveedores')),
    url(r'^turnos/', include('apps.Turn.urls', namespace='Turnos')),
    url(r'^Configuracion/', include('apps.Configuracion.urls', namespace='Configuracion')),
    url(r'^Caja/', include('apps.Caja.urls', namespace='Caja')),
    url(r'^reservas/', include('apps.ReservasWeb.urls', namespace='Reservas')),
    url(r'^admin/', admin.site.urls),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve' , settings.STATIC_ROOT),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', settings.MEDIA_ROOT), 
    url(r'^notificaciones/', include('apps.Notificaciones.urls', namespace='Notificaciones')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),
]
urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)