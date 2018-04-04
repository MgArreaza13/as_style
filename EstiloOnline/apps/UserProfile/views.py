from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
#modelos
from apps.UserProfile.models import tb_profile
#formularios
from apps.UserProfile.forms import UsuarioForm
from apps.UserProfile.forms import ProfileForm
#datos para la vista principal arriba de las citas y los ingresos.
from django.db.models import Count, Min, Sum, Avg
from datetime import date 
from apps.Turn.models import tb_turn
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso
#script de validar el perfil
from apps.scripts.validatePerfil import validatePerfil
#################TASKST################
from apps.Tasks.email_tasks import NuevoPerfilEmail
from apps.Tasks.email_tasks import NuevoUsuarioEmail
# enviar correos
from django.core.mail import send_mail
from django.core.mail import send_mass_mail

# Create your views here.

#Funcion que listara todo los resultados de los usuarios registrados, solo para administradores
@login_required(login_url = 'Demo:login' )
def ListUserProfile(request):
	users = tb_profile.objects.all() #listado completo
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	context  = {
	'perfil':perfil,
	'users':users,
	'perfil':perfil,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	}
	return render(request, 'UserProfile/ListUsers.html', context)

#Funcion para editar un usuario en especifico 
@login_required(login_url = 'Demo:login' )
def EditUserProfile(request , id_UserProfile):
	UserProfile = tb_profile.objects.get(id = id_UserProfile)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	fallido = None
	if request.method == 'GET':
		Form2= ProfileForm(instance=UserProfile)
	else:
		Form2= ProfileForm(request.POST, request.FILES ,instance=UserProfile)
		if  Form2.is_valid():
			UserProfile.user = UserProfile.user
			UserProfile.nameUser = request.POST['nameUser']
			UserProfile.image = request.FILES['image'] 
			UserProfile.birthdayDate = request.POST['birthdayDate']
			UserProfile.save()
			mensaje ="Hemos guardado de manera exitosa todos sus datos" 
			return render (request, 'UserProfile/NuevoUsuario.html', {'Form2':Form2, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'UserProfile/NuevoUsuario.html', {'Form2':Form2, 'perfil':perfil, 'fallido':fallido})

#Funcion para borrar usuarios
@login_required(login_url = 'Demo:login' )
def DeleteUserProfile(request , id_UserProfile):
	UserProfile = tb_profile.objects.get(id = id_UserProfile)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'POST':
		UserProfile.delete()
		mensaje = "hemos borrado su registro de manera exitosa"
		return render (request, 'UserProfile/UserProfileDelete.html', {'UserProfile':UserProfile, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'UserProfile/UserProfileDelete.html', {'UserProfile':UserProfile, 'perfil':perfil,})


#funcion para completar el perfil de los usuarios administradores
@login_required(login_url = 'Demo:login' )
def NuevoPerfil(request):
	Form2 = ProfileForm()
	result = validatePerfil(tb_profile.objects.filter(user__id=request.user.id))
	perfil = result[0]
	fallido = None
	if request.method == 'POST':
		Form2  = ProfileForm(request.POST, request.FILES  or None)
		if Form2.is_valid():
			perfil = Form2.save(commit=False)
			perfil.user = request.user 
			perfil.tipoUser = "Administrador"
			perfil.birthdayDate = request.POST['birthdayDate']
			perfil.save()
			NuevoPerfilEmail.delay(perfil.mailUser, perfil.nameUser )
			mensaje = "Hemos guardado correctamente sus datos"
			return render(request, 'UserProfile/NuevoPerfil.html' , {'Form2':Form2, 'perfil':perfil, 'mensaje':mensaje})
		else:
			Form2	= ProfileForm
			result = validatePerfil(tb_profile.objects.filter(user__id=request.user.id))
			perfil = result[0]
			fallido = "hemos tenido un problema al cargar sus datos, verificalos e intentalo de nuevo"
	return render(request, 'UserProfile/NuevoPerfil.html' , {'Form2':Form2, 'perfil':perfil, 'fallido':fallido})

#funcion que crea el nuevo usuario
@login_required(login_url = 'Demo:login' )
def NuevoUsuario(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	fallido = None
	Form	= UsuarioForm()
	Form2	= ProfileForm()
	if request.method == 'POST':
		Form	= UsuarioForm(request.POST , request.FILES  or None)
		Form2	= ProfileForm(request.POST, request.FILES  or None)
		if Form.is_valid() and Form2.is_valid:
			Form.save()
			usuario = request.POST['username']
			clave 	= request.POST['password1']
			user = auth.authenticate(username=usuario, password=clave)
			if user is not None and user.is_active:
				perfil = Form2.save(commit=False)
				perfil.user = user
				perfil.tipoUser = "Sin Definir"
				perfil.birthdayDate = request.POST['birthdayDate'] 
				perfil.save()
				NuevoUsuarioEmail.delay(perfil.mailUser, perfil.nameUser)
				mensaje = "Hemos guardado correctamente tus datos"
				return render(request, 'UserProfile/NuevoUsuario.html' , {'Form2':Form2 ,'Form':Form , 'perfil':perfil, 'mensaje':mensaje})

		else:
			print('fallido')
			Form	= UsuarioForm(request.POST , request.FILES  or None)
			Form2	= ProfileForm(request.POST, request.FILES  or None)
			fallido = "No pudimos guardar sus datos, intentalo de nuevo luego de verificarlos"
	return render(request, 'UserProfile/NuevoUsuario.html' , {'Form2':Form2 ,'Form':Form , 'perfil':perfil, 'fallido':fallido})


#registro principal 
def Registro(request):
	Form	= UsuarioForm()
	Form2	= ProfileForm()
	if request.method == 'POST':
		Form	= UsuarioForm(request.POST , request.FILES  or None)
		Form2	= ProfileForm(request.POST, request.FILES  or None)
		if Form.is_valid() and Form2.is_valid():
			Form.save()
			usuario = request.POST['username']		
			clave 	= request.POST['password1']
			user = auth.authenticate(username=usuario, password=clave)
			if user is not None and user.is_active:
				perfil = Form2.save(commit=False)
				auth.login(request, user)
				perfil.user = request.user
				perfil.tipoUser = "Sin Definir"
				perfil.birthdayDate = request.POST['birthdayDate']
				perfil.save()
				NuevoUsuarioEmail.delay(perfil.mailUser, perfil.nameUser)
				return redirect ('Clientes:NuevoClientProfile')
		else:
			Form	= UsuarioForm
			Form2	= ProfileForm		
	return render (request, 'UserProfile/registro.html', {'Form':Form , 'Form2':Form2})




#########SERVICIOS############################


from rest_framework import viewsets
from django.contrib.auth.models import User 
from apps.UserProfile.serializers import UserSerializer
from apps.UserProfile.serializers import UserProfileSerializer

class UserViewset(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserProfileViewset(viewsets.ModelViewSet):
	queryset = tb_profile.objects.all()
	serializer_class = UserProfileSerializer