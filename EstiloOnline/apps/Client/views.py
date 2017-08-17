from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Client.models import tb_client
from apps.Client.forms import ClientForm
from apps.Service.models import tb_service
from apps.UserProfile.models import tb_profile
from django.contrib import auth
#datos para la vista principal arriba de las citas y los ingresos.
from django.db.models import Count, Min, Sum, Avg
from datetime import date 
from apps.Turn.models import tb_turn
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso

from apps.UserProfile.forms import UsuarioForm
from apps.UserProfile.forms import ProfileForm
#script de validacion de perfil
from apps.scripts.validatePerfil import validatePerfil


# Create your views here.

#nuevo perfil de cliente
@login_required(login_url = 'Demo:login' )
def NuevoClient(request):
	result = validatePerfil(tb_profile.objects.filter(user__id=request.user.id))
	perfil = result[0]
	Form	= UsuarioForm()
	Form2	= ProfileForm()
	Form3   = ClientForm()
	if request.method == 'POST':
		Form	= UsuarioForm(request.POST , request.FILES  or None)
		Form2	= ProfileForm(request.POST, request.FILES  or None)
		Form3   = ClientForm(request.POST , request.FILES  or None)
		if Form.is_valid() and Form2.is_valid and Form3.is_valid:
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
				perfil.tipoUser = "Cliente"
				perfil.image = request.FILES['image']
				perfil.save()
				cliente = tb_client()
				cliente.user = tb_profile.objects.get(user__id = user.id)
				cliente.dni = request.POST['dni']
				cliente.phoneNumberClient = request.POST['phoneNumberClient']
				cliente.phoneNumberClientTwo = request.POST['phoneNumberClientTwo']
				cliente.addressClient = request.POST['addressClient']
				cliente.addressClientTwo = request.POST['addressClientTwo']
				cliente.save()
				return redirect ('Clientes:ClientesHome')
	else:
		Form	= UsuarioForm
		Form2	= ProfileForm
		Form3   = ClientForm
	return render(request, 'Client/NuevoCliente.html' , {'perfil':perfil, 'Form':Form, 'Form2':Form2, 'Form3':Form3})
@login_required(login_url = 'Demo:login' )
def NuevoClientProfile(request):
	result = validatePerfil(tb_profile.objects.filter(user__id=request.user.id))
	perfil = result[0]
	Form3   = ClientForm()
	if request.method == 'POST':
		Form3   = ClientForm(request.POST , request.FILES  or None)
		if 	Form3.is_valid:
			perfil = tb_profile.objects.get(user_id = request.user.id)
			perfil.tipoUser = "Cliente"
			perfil.save()
			cliente = tb_client()
			cliente.user = tb_profile.objects.get(user__id = request.user.id)
			cliente.dni = request.POST['dni']
			cliente.phoneNumberClient = request.POST['phoneNumberClient']
			cliente.phoneNumberClientTwo = request.POST['phoneNumberClientTwo']
			cliente.addressClient = request.POST['addressClient']
			cliente.addressClientTwo = request.POST['addressClientTwo']
			cliente.save()
			return redirect ('Clientes:ClientesHome')
	else:
		Form2	= ProfileForm
		Form3   = ClientForm
	return render(request, 'Client/NuevoClientProfile.html' , {'perfil':perfil,'Form3':Form3})

#editar cliente 
@login_required(login_url = 'Demo:login' )
def EditClient(request, id_Client):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	ClientEditar = tb_client.objects.get(id=id_Client)
	perfilEditar = tb_profile.objects.get(nameUser = ClientEditar.user)
	if request.method == 'GET':
		Form2	= ProfileForm(instance = perfilEditar)
		Form3 = ClientForm(instance = ClientEditar)
	else:
		Form2 = ProfileForm(request.POST, request.FILES , instance = perfilEditar)
		Form3 = ClientForm(request.POST, request.FILES, instance = ClientEditar)
		if Form2.is_valid and Form3.is_valid():
			perfilEditar.user = perfilEditar.user
			perfilEditar.nameUser = request.POST['nameUser']
			perfilEditar.image = request.FILES['image'] 
			perfilEditar.mailUser = request.POST['mailUser']
			perfilEditar.birthdayDate = request.POST['birthdayDate']
			perfilEditar.save()
			Form3.save()
			return redirect ('Clientes:list')
	return render (request, 'Client/NuevoCliente.html' , {'Form3':Form3 , 'Form2':Form2 , 'perfil':perfil})

#listado de los clientes en la parte principal
@login_required(login_url = 'Demo:login' )
def Clientes(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	servicios = tb_service.objects.all()[:10]
	clientes = tb_client.objects.all()[:8] 
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	context ={
	'perfil':perfil,
	'clientes':clientes,
	'servicios':servicios,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,


	}
	return render(request ,'Client/clients.html', context )

#perfil del cliente 
@login_required(login_url = 'Demo:login' )
def ClienteProfile(request, id_Client):
	cliente = tb_client.objects.get(id=id_Client)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]

	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	citas_total = tb_turn.objects.filter(client__id = id_Client).count()
	En_Proceso = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Proceso").count()
	citas_atendidas = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Atendido").count()
	turnos_en_espera = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Espera").count()
	turnos_cancelados = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Cancelado").count()
	context = {
	'perfil':perfil,
	'cliente':cliente,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'citas_atendidas':citas_atendidas,
	'turnos_en_espera':turnos_en_espera,
	'turnos_cancelados':turnos_cancelados,
	'citas_total':citas_total,
	'En_Proceso':En_Proceso
	}
	return render(request ,'Client/ClientDetail.html', context )

#citas pedidas por el cliente
@login_required(login_url = 'Demo:login' )
def CitasPedidasClient(request, id_Client):
	client = tb_client.objects.get(id= id_Client)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	turnos = tb_turn.objects.filter(client__id = id_Client)
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	citas_total = tb_turn.objects.filter(client__id = id_Client).count()
	En_Proceso = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Proceso").count()
	citas_atendidas = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Atendido").count()
	turnos_en_espera = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Espera").count()
	turnos_cancelados = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Cancelado").count()
	
	context = { 
	'perfil':perfil,
	'client':client,
	'turnos':turnos,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'citas_atendidas':citas_atendidas,
	'turnos_en_espera':turnos_en_espera,
	'turnos_cancelados':turnos_cancelados,
	'citas_total':citas_total,
	'En_Proceso':En_Proceso
	}
	return render (request  , 'Client/CitasPedidasClient.html' , context)

#historial de todas las citas del cliente
@login_required(login_url = 'Demo:login' )
def HistorialCitasClient(request, id_Client):
	client = tb_client.objects.get(id= id_Client)
	turnos = tb_turn.objects.filter(client__id = id_Client)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	citas_total = tb_turn.objects.filter(client__id = id_Client).count()
	En_Proceso = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Proceso").count()
	citas_atendidas = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Atendido").count()
	turnos_en_espera = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Espera").count()
	turnos_cancelados = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Cancelado").count()
	
	context = {
	'perfil':perfil,
	'client':client,
	'turnos':turnos,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'citas_atendidas':citas_atendidas,
	'turnos_en_espera':turnos_en_espera,
	'turnos_cancelados':turnos_cancelados,
	'citas_total':citas_total,
	'En_Proceso':En_Proceso
	}
	return render (request  , 'Client/HistorialClient.html' , context)

#citas atendidas del cliente
@login_required(login_url = 'Demo:login' )
def CitasAtendidasClient(request, id_Client):
	client = tb_client.objects.get(id= id_Client)
	turnos = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Atendido")
	#queryset 
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	citas_total = tb_turn.objects.filter(client__id = id_Client).count()
	En_Proceso = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Proceso").count()
	citas_atendidas = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Atendido").count()
	turnos_en_espera = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Espera").count()
	turnos_cancelados = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Cancelado").count()
	
	context = {
	'perfil':perfil,
	'client':client,
	'turnos':turnos,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'citas_atendidas':citas_atendidas,
	'turnos_en_espera':turnos_en_espera,
	'turnos_cancelados':turnos_cancelados,
	'citas_total':citas_total,
	'En_Proceso':En_Proceso
	}
	return render (request  , 'Client/CitasAtendidasClient.html' , context)

#citas que tiene el cliente en proceso
@login_required(login_url = 'Demo:login' )
def CitasEnProcesoClient(request, id_Client):
	client = tb_client.objects.get(id= id_Client)
	turnos = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Proceso")
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	citas_total = tb_turn.objects.filter(client__id = id_Client).count()
	En_Proceso = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Proceso").count()
	citas_atendidas = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Atendido").count()
	turnos_en_espera = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Espera").count()
	turnos_cancelados = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Cancelado").count()
	
	context = {
	'perfil':perfil,
	'client':client,
	'turnos':turnos,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'citas_atendidas':citas_atendidas,
	'turnos_en_espera':turnos_en_espera,
	'turnos_cancelados':turnos_cancelados,
	'citas_total':citas_total,
	'En_Proceso':En_Proceso
	}
	return render (request  , 'Client/CitasEnProcesoClient.html' , context)


#Citas que el cliente tiene en espera
@login_required(login_url = 'Demo:login' )
def CitasEnEsperaClient(request, id_Client):
	client = tb_client.objects.get(id= id_Client)
	turnos = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Espera")
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	citas_total = tb_turn.objects.filter(client__id = id_Client).count()
	En_Proceso = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Proceso").count()
	citas_atendidas = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Atendido").count()
	turnos_en_espera = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Espera").count()
	turnos_cancelados = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Cancelado").count()
	
	context = {
	'perfil':perfil,
	'client':client,
	'turnos':turnos,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'citas_atendidas':citas_atendidas,
	'turnos_en_espera':turnos_en_espera,
	'turnos_cancelados':turnos_cancelados,
	'citas_total':citas_total,
	'En_Proceso':En_Proceso
	}
	return render (request  , 'Client/CitasEnEsperaClient.html' , context)

#citas canceladas del cliente
@login_required(login_url = 'Demo:login' )
def CitasCanceladasClient(request, id_Client):
	client = tb_client.objects.get(id= id_Client)
	turnos = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Cancelado")
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	citas_total = tb_turn.objects.filter(client__id = id_Client).count()
	En_Proceso = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Proceso").count()
	citas_atendidas = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Atendido").count()
	turnos_en_espera = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "En Espera").count()
	turnos_cancelados = tb_turn.objects.filter(client__id = id_Client).filter(statusTurn__nameStatus= "Cancelado").count()
	
	context = {
	'perfil':perfil,
	'client':client,
	'turnos':turnos,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'citas_atendidas':citas_atendidas,
	'turnos_en_espera':turnos_en_espera,
	'turnos_cancelados':turnos_cancelados,
	'citas_total':citas_total,
	'En_Proceso':En_Proceso
	}
	return render (request  , 'Client/CitasCanceladoClient.html' , context)




#listado de todos los clientes para el administrador
@login_required(login_url = 'Demo:login' )
def list(request):
	clientes =  tb_client.objects.all()
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]

	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	context = {
	'clientes':clientes,
	'perfil':perfil,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,



	}
	return render(request,'Client/ListClients.html', context )






@login_required(login_url = 'Demo:login' )
def DeleteClient(request , id_Client):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	ClientBorrar= tb_client.objects.get(id=id_Client)
	if request.method == 'POST':
		ClientBorrar.delete()
		return redirect ('Clientes:list')
	return render (request, 'Client/DeleteCliente.html', {'ClientBorrar':ClientBorrar, 'perfil':perfil})