from django.conf.urls import url
from django.contrib import admin
from apps.Collaborator.views import ListColaboradores
from apps.Collaborator.views import NuevoColaborador
from apps.Collaborator.views import EditarColaborador
from apps.Collaborator.views import EliminarColaborador
from apps.Collaborator.views import ColaboradorProfile
from apps.Collaborator.views import HistorialCollaborador
from apps.Collaborator.views import agenda
from apps.Collaborator.views import turnos
from apps.Collaborator.views import editTurnosColaborador
from apps.Collaborator.views import ColaboradorDetail
from apps.Collaborator.views import SimpleRegister
from apps.Collaborator.views import CompletarPerfilColaborador

urlpatterns = [

	#url(r'^$', Clientes , name='ClientesHome'  ),
	url(r'^Perfil/(?P<id_colaborador>\d+)$', ColaboradorProfile , name='ColaboradorProfile' ),
	url(r'^list/$', ListColaboradores , name='ListColaboradores'  ),
	url(r'^Nuevo/$', NuevoColaborador , name='NuevoColaborador'  ),
	url(r'^turnos/(?P<id_colaborador>\d+)$', turnos , name='turnos'  ),
	url(r'^turnos/(?P<id_colaborador>\d+)/(?P<id_turn>\d+)$', editTurnosColaborador , name='editTurnosColaborador'  ),
	url(r'^Historial/(?P<id_colaborador>\d+)$', HistorialCollaborador, name='HistorialCollaborador'  ),
	url(r'^Agenda/(?P<id_colaborador>\d+)$', agenda, name='agenda'  ),
	url(r'^Editar/(?P<id_colaborador>\d+)$', EditarColaborador, name='EditarColaborador'  ),
	url(r'^Borrar/(?P<id_colaborador>\d+)$', EliminarColaborador, name='EliminarColaborador'  ),
  	url(r'^Consulta/colaborador/detalles/de/monto$', ColaboradorDetail, name='ColaboradorDetail'  ),
  	url(r'^Nuevo/Registro$', SimpleRegister, name='SimpleRegister'  ),
	url(r'^Nuevo/Perfil/de/colaborador$', CompletarPerfilColaborador, name='CompletarPerfilColaborador'  ),
]