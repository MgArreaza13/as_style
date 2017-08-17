from django.conf.urls import url
from django.contrib import admin
from apps.PanelPrincipal.views import inicio





from apps.PanelPrincipal.views import calendario 
from apps.PanelPrincipal.views import login
from apps.PanelPrincipal.views import logout 

from apps.PanelPrincipal.views import loockscreen

from apps.PanelPrincipal.views import ingresosegresos

from apps.PanelPrincipal.views import registro




app_name = 'Demo'

urlpatterns = [
	url(r'^$', inicio, name='inicio' ),
	url(r'^entrar/$', login, name='login' ),
	url(r'^salir/$', logout, name='logout' ),
	
	
	
	
	
	
	
	
	
	url(r'^calendario/$', calendario, name='calendario' ),

	
	
	url(r'^ingresosegresos/$', ingresosegresos, name='ingresoegresos' ),

	
	


	url(r'^bloqueado/$', loockscreen ,  name='bloqueado' ),
	url(r'^registro/$', registro ),
  
]