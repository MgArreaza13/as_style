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
#rest framework
from rest_framework import routers
router =  routers.DefaultRouter()
#modulos 

#Colaboradores
from apps.Collaborator.views import CollaboratorViewset
router.register(r'api/colaboradores', CollaboratorViewset)

from apps.Collaborator.views import typeCollaboratorViewset
from apps.Collaborator.views import UserProfileViewset


router.register(r'tiposcolaboradores2', typeCollaboratorViewset)
router.register(r'user2', UserProfileViewset)

urlpatterns = [
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
    url(r'^admin/', admin.site.urls),
    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve' , settings.STATIC_ROOT),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', settings.MEDIA_ROOT), 
    url('', include('social.apps.django_app.urls', namespace='social')),
]
urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)