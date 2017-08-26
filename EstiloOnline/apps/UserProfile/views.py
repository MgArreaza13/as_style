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
			#mandar mensaje de nuevo usuario
			#Enviaremos los correos a el colaborador y al cliente 
			#colaborador
			usuario = perfil.mailUser #trato de traer el colaborador del formulario
			email_subject_usuario = 'Estilo Online Nuevo Cliente'
			email_body_usuario = "Hola %s, gracias por crearte un nuevo perfil de cliente, ya puedes crear nuevos turnos y muchas cosas mas para mas informacion ingrese aqui http://estiloonline.pythonanywhere.com" %(perfil.nameUser)
			message_usuario = (email_subject_usuario, email_body_usuario , 'as.estiloonline@gmail.com', [usuario])
			#mensaje para apreciasoft
			email_subject_Soporte = 'Nuevo perfil de clientes Registrado'
			email_body_Soporte = "se ha registrado un nuevo perfil de cliente con nombre %s para verificar ingrese aqui http://estiloonline.pythonanywhere.com" %(perfil.nameUser)
			message_Soporte = (email_subject_Soporte, email_body_Soporte , 'as.estiloonline@gmail.com', ['soporte@apreciasoft.com'])
			#enviamos el correo
			send_mass_mail((message_usuario, message_Soporte), fail_silently=False)
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
	fallido - None
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
				#mandar mensaje de nuevo usuario
				#Enviaremos los correos a el colaborador y al cliente 
				#colaborador
				usuario = perfil.mailUser #trato de traer el colaborador del formulario
				email_subject_usuario = 'Bienvenido a Estilo Online'
				email_body_usuario = "Hola %s, te damos una cordial bienvenida a nuestro sistema esperemos que tengas una experiencia agradable con nuestro sistema, para sacarle el maximo provecho ingrese aqui http://estiloonline.pythonanywhere.com" %(perfil.nameUser)
				message_usuario = (email_subject_usuario, email_body_usuario , 'as.estiloonline@gmail.com', [usuario])
				#mensaje para apreciasoft
				email_subject_Soporte = 'Nuevo Usuario Registrado'
				email_body_Soporte = "se ha registrado un nuevo usuario de nombre %spara verificar ingrese aqui http://estiloonline.pythonanywhere.com" %(perfil.nameUser)
				message_Soporte = (email_subject_Soporte, email_body_Soporte , 'as.estiloonline@gmail.com', ['soporte@apreciasoft.com'])
				#enviamos el correo
				send_mass_mail((message_usuario, message_Soporte), fail_silently=False)
				mensaje = "Hemos guardado correctamente tus datos"

				return render(request, 'UserProfile/NuevoUsuario.html' , {'Form2':Form2 ,'Form':Form , 'perfil':perfil, 'mensaje':mensaje})

	else:
		Form	= UsuarioForm
		Form2	= ProfileForm
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
				#mandar mensaje de nuevo usuario
				#Enviaremos los correos a el colaborador y al cliente 
				#colaborador
				usuario = perfil.mailUser #trato de traer el colaborador del formulario
				email_subject_usuario = 'Bienvenido a Estilo Online'
				email_body_usuario = "Hola %s, te damos una cordial bienvenida a nuestro sistema esperemos que tengas una experiencia agradable con nuestro sistema, para sacarle el maximo provecho ingrese aqui http://estiloonline.pythonanywhere.com" %(perfil.nameUser)
				message_usuario = (email_subject_usuario, email_body_usuario , 'as.estiloonline@gmail.com', [usuario])
				#mensaje para apreciasoft
				email_subject_Soporte = 'Nuevo Usuario Registrado'
				email_body_Soporte = "se ha registrado un nuevo usuario de nombre %spara verificar ingrese aqui http://estiloonline.pythonanywhere.com" %(perfil.nameUser)
				message_Soporte = (email_subject_Soporte, email_body_Soporte , 'as.estiloonline@gmail.com', ['soporte@apreciasoft.com'])
				#enviamos el correo
				send_mass_mail((message_usuario, message_Soporte), fail_silently=False)
				return redirect ('Clientes:NuevoClientProfile')
		else:
			Form	= UsuarioForm
			Form2	= ProfileForm		
	return render (request, 'UserProfile/registro.html', {'Form':Form , 'Form2':Form2})