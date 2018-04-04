from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Collaborator.models import tb_collaborator
from apps.Collaborator.forms import ColaboradorForm
from django.contrib import auth
# Create your views here.

#datos para la vista principal arriba de las citas y los ingresos.
from django.db.models import Count, Min, Sum, Avg
from datetime import date 
from apps.Turn.models import tb_turn
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso
from apps.Turn.forms import EditTurnForm
from apps.UserProfile.models import tb_profile
from apps.scripts.validatePerfil import validatePerfil
from apps.UserProfile.forms import UsuarioForm
from apps.UserProfile.forms import ProfileForm
from apps.ReservasWeb.models import tb_reservasWeb
from apps.Configuracion.models import tb_status
# enviar correos
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.http import JsonResponse
from django.core import serializers
from apps.Caja.models import tb_egreso_colaborador
from apps.Configuracion.models import tb_formasDePago
from apps.Tasks.email_tasks import PerfilColaboradorMail




def ColaboradorDetail(request):
	id_colaborador = request.GET.get('id', None)
	colaborador_data = tb_collaborator.objects.get(id = id_colaborador)
	imagen = str(colaborador_data.user.image)
	pagos_realizados = serializers.serialize('json', tb_egreso_colaborador.objects.filter(colaborador = id_colaborador), fields=('descripcion','monto','dateCreate'))
	reservas = serializers.serialize('json', tb_reservasWeb.objects.filter(collaborator__id = id_colaborador), fields=('montoAPagar','nombre','dateTurn'))
	
	data = {
		'id':colaborador_data.id,
		'nombre':colaborador_data.user.nameUser,
		'monto':colaborador_data.MontoAcumulado,
		'imagen':imagen,
		'reservas':reservas,
		'pagos_realizados':pagos_realizados,
		
	}
	return JsonResponse(data)


@login_required(login_url = 'Demo:login' )
def CompletarPerfilColaborador(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form2 = ProfileForm()
	Form3 = ColaboradorForm()
	fallido = None
	if request.method == 'POST':
		Form2 = ProfileForm(request.POST , request.FILES or None)
		Form3 = ColaboradorForm(request.POST , request.FILES or None)
		if  Form2.is_valid() and Form3.is_valid():
			perfil = tb_profile.objects.get(user = request.user)
			perfil.nameUser = request.POST['nameUser']
			perfil.mailUser = request.POST['mailUser']
			perfil.birthdayDate = request.POST['birthdayDate']
			perfil.tipoUser = "Colaborador"
			perfil.image = request.FILES['image']
			perfil.save()
			colaborador = Form3.save(commit=False)
			colaborador.user = tb_profile.objects.get(user = request.user)
			colaborador.save()
			PerfilColaboradorMail.delay(perfil.mailUser, perfil.nameUser)
			mensaje = "Hemos Registrado Su nuevo colaborador de manera exitosa"
			return redirect ('Panel:inicio')
			#return render(request, 'Collaborator/NuevoCollaborador.html' , {'Form':Form , 'Form2':Form2, 'Form3':Form3, 'perfil':perfil, 'mensaje':mensaje})
		else:
			Form = UsuarioForm(request.POST , request.FILES or None)
			Form2 = ProfileForm(request.POST , request.FILES or None)
			Form3 = ColaboradorForm(request.POST , request.FILES or None)
			
			fallido = "hemos tenido problemas al cargar los datos , verifiquelos e intente de nuevo"
	return render(request, 'Collaborator/NuevoCollaborador.html' , { 'Form2':Form2, 'Form3':Form3, 'perfil':perfil, 'fallido':fallido})





@login_required(login_url = 'Demo:login' )
def SimpleRegister(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = UsuarioForm()
	fallido = None
	if request.method == 'POST':
		Form = UsuarioForm(request.POST , request.FILES or None)
		
		if Form.is_valid():
			Form.save()
			usuario = request.POST['username']
			clave 	= request.POST['password1']
			user = auth.authenticate(username=usuario, password=clave)
			perfil = tb_profile()
			perfil.user = user
			perfil.tipoUser = 'Colaborador'
			perfil.birthdayDate = '1995-04-19'
			perfil.save()
			return redirect ('Colaboradores:ListColaboradores')
		else:
			Form = UsuarioForm(request.POST , request.FILES or None)		
			fallido = "hemos tenido problemas al cargar los datos , verifiquelos e intente de nuevo"
	return render(request, 'Collaborator/simplecolaborador.html' , {'Form':Form ,  'perfil':perfil, 'fallido':fallido})




#vista para crear el nuevo colaborador
@login_required(login_url = 'Demo:login' )
def NuevoColaborador(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = UsuarioForm()
	Form2 = ProfileForm()
	Form3 = ColaboradorForm()
	fallido = None
	if request.method == 'POST':
		Form = UsuarioForm(request.POST , request.FILES or None)
		Form2 = ProfileForm(request.POST , request.FILES or None)
		Form3 = ColaboradorForm(request.POST , request.FILES or None)
		if Form.is_valid() and Form2.is_valid() and Form3.is_valid():
			Form.save()
			usuario = request.POST['username']
			clave 	= request.POST['password1']
			user = auth.authenticate(username=usuario, password=clave)
			if user is not None and user.is_active:
				perfil = tb_profile()
				perfil.user = user
				perfil.nameUser = request.POST['nameUser']
				perfil.mailUser = request.POST['mailUser']
				perfil.birthdayDate = request.POST['birthdayDate']
				perfil.tipoUser = "Colaborador"
				perfil.image = request.FILES['image']
				perfil.save()
				colaborador = Form3.save(commit=False)
				colaborador.user = tb_profile.objects.get(user__id = user.id)
				colaborador.save()
				PerfilColaboradorMail.delay(perfil.mailUser, perfil.nameUser)
				mensaje = "Hemos Registrado Su nuevo colaborador de manera exitosa"
				return redirect ('Colaboradores:ListColaboradores')
				return render(request, 'Collaborator/NuevoCollaborador.html' , {'Form':Form , 'Form2':Form2, 'Form3':Form3, 'perfil':perfil, 'mensaje':mensaje})
		else:
			Form = UsuarioForm(request.POST , request.FILES or None)
			Form2 = ProfileForm(request.POST , request.FILES or None)
			Form3 = ColaboradorForm(request.POST , request.FILES or None)
			
			fallido = "hemos tenido problemas al cargar los datos , verifiquelos e intente de nuevo"
	return render(request, 'Collaborator/NuevoCollaborador.html' , {'Form':Form , 'Form2':Form2, 'Form3':Form3, 'perfil':perfil, 'fallido':fallido})




#Editar Colaborador
@login_required(login_url = 'Demo:login' )
def EditarColaborador(request, id_colaborador):
	
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	ColaboradorEditar= tb_collaborator.objects.get(id=id_colaborador)
	perfilEditar = tb_profile.objects.get(nameUser = ColaboradorEditar.user)
	fallido = None
	if request.method == 'GET':
		Form2	= ProfileForm(instance = perfilEditar)
		Form3= ColaboradorForm(instance = ColaboradorEditar)
	else:
		Form2 = ProfileForm(request.POST, request.FILES , instance = perfilEditar)
		Form3 = ColaboradorForm(request.POST, request.FILES  ,  instance = ColaboradorEditar)
		if Form2.is_valid() and Form3.is_valid():
			perfilEditar.user = perfilEditar.user
			perfilEditar.nameUser = request.POST['nameUser']
			perfilEditar.image = request.FILES['image'] 
			perfilEditar.mailUser = request.POST['mailUser']
			perfilEditar.birthdayDate = request.POST['birthdayDate']
			perfilEditar.save()
			Form3.save()
			mensaje = "Hemos Guardado de Manera Exitosa sus nuevos datos"
			return render (request, 'Collaborator/NuevoCollaborador.html' , {'Form3':Form3 , 'Form2':Form2, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'Collaborator/NuevoCollaborador.html' , {'Form3':Form3 , 'Form2':Form2, 'perfil':perfil, 'fallido':fallido})

#listado de los colaboradores
@login_required(login_url = 'Demo:login' )
def ListColaboradores(request):
	formas_de_pago = tb_formasDePago.objects.all()
	colaboradores = tb_collaborator.objects.all()
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	context = {
	'formas_de_pago':formas_de_pago,
	'perfil':perfil,
	'colaboradores':colaboradores,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	}
	return render(request , 'Collaborator/ListCollaborator.html' , context)



@login_required(login_url = 'Demo:login' )
def HistorialCollaborador(request, id_colaborador):
	
	collaborador = tb_collaborator.objects.get(id = id_colaborador )
	turnos = tb_turn.objects.filter(collaborator_id = id_colaborador).order_by('dateTurn','dateTurn' )
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	context = {
	
	'perfil':perfil,
	'collaborador':collaborador,
	'turnos':turnos,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	}
	return render(request , 'Collaborator/HistorialCollaborador.html' , context)



@login_required(login_url = 'Demo:login' )
def ColaboradorProfile(request, id_colaborador):
	
	colaborador = tb_collaborator.objects.get(user__user_id=id_colaborador)
	citas_atendidas = tb_turn.objects.filter(collaborator__user_id = id_colaborador).filter(statusTurn__nameStatus= "Atendido").count()
	turnos_en_espera = tb_turn.objects.filter(collaborator__user_id = id_colaborador).filter(statusTurn__nameStatus= "En Espera").count()
	turnos_cancelados = tb_turn.objects.filter(collaborator__user_id = id_colaborador).filter(statusTurn__nameStatus= "Cancelado").count()
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	context = {
	
	'perfil':perfil,
	'colaborador':colaborador,
	'citas_atendidas':citas_atendidas,
	'turnos_en_espera':turnos_en_espera,
	'turnos_cancelados':turnos_cancelados,
	}
	return render(request , 'Collaborator/Profile.html' ,context)	




@login_required(login_url = 'Demo:login' )
def EliminarColaborador(request, id_colaborador):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	colaboradorBorrar= tb_collaborator.objects.get(id=id_colaborador)
	fallido = None
	if request.method == 'POST':
		colaboradorBorrar.delete()
		mensaje =  "Hemos Borrado de manera Exitosa su registro"
		return render (request, 'Collaborator/CollaboradorBorrar.html', {'colaboradorBorrar':colaboradorBorrar, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'Collaborator/CollaboradorBorrar.html', {'colaboradorBorrar':colaboradorBorrar, 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def agenda (request, id_colaborador):
	turnos =  tb_turn.objects.filter(collaborator__user_id = id_colaborador).filter(statusTurn__nameStatus="En Espera")
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	
	fecha = date.today()
	perfil = result[0]
	context = {
	
	'turnos':turnos,
	'perfil':perfil,
	}
	return render (request , 'Collaborator/Agenda.html', context)

@login_required(login_url = 'Demo:login' )
def turnos (request, id_colaborador):
	collaborador = tb_collaborator.objects.get(user__user_id = id_colaborador)
	turnos = tb_turn.objects.filter(collaborator__user_id = id_colaborador).order_by('dateTurn','dateTurn' )
	reservas = tb_reservasWeb.objects.filter(collaborator__user_id = id_colaborador).order_by('dateTurn','dateTurn' )
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	status = tb_status.objects.all()
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	context = {
	'status':status,
	'reservas':reservas,
	'turnos':turnos,
	'collaborador':collaborador,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'perfil':perfil,
	}
	return render(request,'Collaborator/turnos.html', context)


#vista para editar los turnos del colaborador en sesion 
@login_required(login_url = 'Demo:login' )
def editTurnosColaborador (request, id_colaborador, id_turn):
	collaborador = tb_collaborator.objects.get(user__user_id = id_colaborador)
	turnos = tb_turn.objects.filter(collaborator__user_id = id_colaborador).order_by('dateTurn','dateTurn' )
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	formulario = True
	TurnEditar = tb_turn.objects.get(id = id_turn)
	if request.method == 'GET':
		idturn = id_turn
		Form= EditTurnForm(instance=TurnEditar)
	else:
		idturn = id_turn
		Form= EditTurnForm(request.POST,instance=TurnEditar)
		if  Form.is_valid():
			turno 		 = Form.save(commit=False)
			turno.user	 = request.user
			turno.dateTurn = TurnEditar.dateTurn
			turno.HoraTurn = TurnEditar.HoraTurn
			turno.client = TurnEditar.client
			turno.collaborator = TurnEditar.collaborator
			turno.extraInfoTurn = TurnEditar.extraInfoTurn
			turno.servicioPrestar = TurnEditar.servicioPrestar
			turno.isPay = TurnEditar.isPay
			turno.save()
			return redirect ('Panel:inicio')

	context = {
	'perfil':perfil,
	'Form':Form ,
	'TurnEditar':TurnEditar,
	'turnos':turnos,
	'collaborador':collaborador,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'perfil':perfil,
	}
	return render(request,'Collaborator/turnos.html', context)
	



#########################SERVICiOS################################
from apps.Collaborator.serializers import CollaboratorSerializer

from rest_framework import viewsets	

	
class CollaboratorViewset(viewsets.ModelViewSet):
	queryset = tb_collaborator.objects.all()
	serializer_class = CollaboratorSerializer

