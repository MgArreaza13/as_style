from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from datetime import date
#Modelos 
from apps.Turn.models import tb_turn
from apps.Collaborator.models import tb_collaborator
from apps.Turn.models import tb_turn
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso
#FORMULARIOS
from apps.Turn.forms import TurnForm
from apps.Turn.forms import EditTurnForm
#datos para la vista principal arriba de las citas y los ingresos.
from django.db.models import Count, Min, Sum, Avg
from datetime import date 
# Create your views here.
from apps.UserProfile.models import tb_profile
from apps.scripts.validatePerfil import validatePerfil
# enviar correos
from django.core.mail import send_mail
from django.core.mail import send_mass_mail


#Resumen de todos los turnos, parte principal
@login_required(login_url = 'Demo:login' )
def index(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	fecha =  date.today()
	TurnEditar = -1 #para poder saber que turnos se le mostrara el formulario, verifico que ningun id coincida con -1
	is_collaborador = tb_collaborator.objects.filter(user__id = request.user.id) #saber si el usuario actual es collaborador
	turnos = tb_turn.objects.filter(dateTurn = fecha).order_by('HoraTurn')
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	context = {
	'perfil':perfil,
	'is_collaborador':is_collaborador,
	'turnos':turnos,
	'fecha':fecha, 
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'TurnEditar':TurnEditar

	}
	return render(request,'Turn/ResumenTurnos.html', context )

#Crea El turno para la fecha actual
@login_required(login_url = 'Demo:login' )
def NuevoTurnParaHoy(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	turnos = tb_turn.objects.filter(statusTurn__nameStatus="En Espera")
	perfil = result[0]
	Form = TurnForm
	fecha =  date.today()
	mensaje1 = None
	fallido = None
	if request.method == 'POST':
		Form = TurnForm(request.POST or None)
		fecha =  date.today()
		colaboradorOcupado = tb_turn.objects.filter(dateTurn=fecha).filter(statusTurn__nameStatus="En Espera").filter(HoraTurn=request.POST['TimeTurn']).filter(collaborator=request.POST['collaborator'])	
		data = len(colaboradorOcupado)
		if Form.is_valid():
			if data == 0: #no encontro un collaborador ocupado para ese dia y hora
				turno = Form.save(commit=False)
				turno.user = request.user
				turno.dateTurn = fecha
				turno.HoraTurn = request.POST['TimeTurn']
				if request.POST['extraInfoTurn'] == "":
					turno.extraInfoTurn = 'Sin Comentarios'
				else:
					turno.extraInfoTurn = request.POST['extraInfoTurn']
				#Envio de mensajes 
				colaborador = tb_profile.objects.get(nameUser=turno.collaborator) #trato de traer el colaborador del formulario
				email_subject_Colaborador = 'Nuevo Turno Solicitado Por Cliente'
				email_body_Colaborador = "Hola %s, El presente mensaje es para informarle que ha recibido una nueva solicitud para un turno si desea revisarla y confirmarla ingrese aqui http://estiloonline.pythonanywhere.com" %(colaborador)
				email_colaborador = colaborador.mailUser
				message_colaborador = (email_subject_Colaborador, email_body_Colaborador , 'as.estiloonline@gmail.com', [email_colaborador])
				#cliente
				client = tb_profile.objects.get(user__username=turno.client) #trato de traer el colaborador del formulario
				email_subject_client = 'Nuevo Turno Solicitado'
				email_body_Client = "Hola %s, El presente mensaje es para informarle que se ha enviado una nueva solicitud para un turno si desea revisarla y confirmarla ingrese aqui http://estiloonline.pythonanywhere.com" %(client)
				email_client = client.mailUser
				message_client = (email_subject_client, email_body_Client, 'as.estiloonline@gmail.com', [email_client])
				#mensaje para apreciasoft
				email_subject_Soporte = 'Nuevo Turno Solicitado en Estilo Online'
				email_body_Soporte = "Hola, soporte Apreciasoft, El presente mensaje es para informarle que el cliente  %s ha enviado una nueva solicitud para de turno para el colaborador %s , si desea revisarla ingrese aqui http://estiloonline.pythonanywhere.com" %(client,colaborador)
				message_Soporte = (email_subject_Soporte, email_body_Soporte , 'as.estiloonline@gmail.com', ['soporte@apreciasoft.com'])
				#enviamos el correo
				send_mass_mail((message_colaborador, message_client, message_Soporte), fail_silently=False)
				turno.save()
				mensaje = 'Felicidades Hemos podido guardar su turno de manera exitosa'
				return render(request, 'Turn/NuevoTurnoHoy.html' , {'Form':Form,'turnos':turnos ,'fecha':fecha , 'mensaje1':mensaje1, 'perfil':perfil, 'mensaje':mensaje})
			elif data == 1: # collaborador ocupado para esa hora y fecha
				mensaje1 = "El Colaborador que desea Contratar esta Ocupado Para El Dia y la hora deseado intente con otro collaborador o con otro dia"
				Form = TurnForm()
				fallido = "No hemos podido cargar sus datos correctamente, verifique e intente nuevamente"
		else:
			mensaje = "Errores en los datos Verifiquelos, y vuelva a intentarlo"
			fecha =  date.today()
			Form = TurnForm()
			fallido = "No hemos podido cargar sus datos correctamente, verifique e intente nuevamente"

	
	return render(request, 'Turn/NuevoTurnoHoy.html' , {'Form':Form,'turnos':turnos ,'fecha':fecha , 'mensaje1':mensaje1, 'perfil':perfil, 'fallido':fallido})


#Edita los Status de los turnos
@login_required(login_url = 'Demo:login' )
def EditTurnStatus(request , id_turn):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	turnos = tb_turn.objects.filter(dateTurn = date.today()).order_by('HoraTurn')
	TurnEditar = tb_turn.objects.get(id = id_turn)
	fallido = None
	if request.method == 'GET':
		Form= EditTurnForm(instance=TurnEditar)
	else:
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
			turno.isProcessClient = TurnEditar.isProcessClient
			turno.isProcessCollaborator = TurnEditar.isProcessCollaborator
			turno.save()
			mensaje = "hemos cargado sus nuevos datos de manera exitosa"
			return render (request, 'Turn/ResumenTurnos.html', {'turnos':turnos,'Form':Form, 'TurnEditar':TurnEditar, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'Turn/ResumenTurnos.html', {'turnos':turnos,'Form':Form, 'TurnEditar':TurnEditar, 'perfil':perfil, 'fallido':fallido})


#lista todo los turnos en la tabla
@login_required(login_url = 'Demo:login' )
def listTurnos(request):
	TurnEditar = -1 #para poder saber que turnos se le mostrara el formulario, verifico que ningun id coincida con -1
	turnos = tb_turn.objects.all().order_by('dateTurn')
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	formulario = False
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	context = {
	'perfil':perfil,
	'turnos':turnos,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	'TurnEditar':TurnEditar,

	}
	return render(request,'Turn/ListaDeTurnos.html',context )

#crea los turnos
@login_required(login_url = 'Demo:login' )
def NuevoTurn(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	turnos = tb_turn.objects.filter(statusTurn__nameStatus="En Espera")
	perfil = result[0]
	Form = TurnForm
	mensaje1 = None
	fallido = None
	if request.method == 'POST':
		Form = TurnForm(request.POST or None)
		colaboradorOcupado = tb_turn.objects.filter(dateTurn=request.POST['TurnDate']).filter(statusTurn__nameStatus="En Espera").filter(HoraTurn=request.POST['TimeTurn']).filter(collaborator=request.POST['collaborator'])	
		data = len(colaboradorOcupado)
		if Form.is_valid():
			if data == 0: #no encontro un collaborador ocupado para ese dia y hora 
				turno = Form.save(commit=False)
				turno.user = request.user
				turno.dateTurn = request.POST['TurnDate']
				turno.HoraTurn = request.POST['TimeTurn']
				if request.POST['extraInfoTurn'] == "":
					turno.extraInfoTurn = 'Sin Comentarios'
				else:
					turno.extraInfoTurn = request.POST['extraInfoTurn']
				turno.save()
				#Enviaremos los correos a el colaborador y al cliente 
				#colaborador
				colaborador = tb_profile.objects.get(nameUser=turno.collaborator) #trato de traer el colaborador del formulario
				email_subject_Colaborador = 'Nuevo Turno Solicitado Por Cliente'
				email_body_Colaborador = "Hola %s, El presente mensaje es para informarle que ha recibido una nueva solicitud para un turno si desea revisarla y confirmarla ingrese aqui http://estiloonline.pythonanywhere.com" %(colaborador)
				email_colaborador = colaborador.mailUser
				message_colaborador = (email_subject_Colaborador, email_body_Colaborador , 'as.estiloonline@gmail.com', [email_colaborador])
				#cliente
				client = tb_profile.objects.get(user__username=turno.client) #trato de traer el colaborador del formulario
				email_subject_client = 'Nuevo Turno Solicitado'
				email_body_Client = "Hola %s, El presente mensaje es para informarle que se ha enviado una nueva solicitud para un turno si desea revisarla y confirmarla ingrese aqui http://estiloonline.pythonanywhere.com" %(client)
				email_client = client.mailUser
				message_client = (email_subject_client, email_body_Client, 'as.estiloonline@gmail.com', [email_client])
				#mensaje para apreciasoft
				email_subject_Soporte = 'Nuevo Turno Solicitado en Estilo Online'
				email_body_Soporte = "Hola, soporte Apreciasoft, El presente mensaje es para informarle que el cliente  %s ha enviado una nueva solicitud para de turno para el colaborador %s , si desea revisarla ingrese aqui http://estiloonline.pythonanywhere.com" %(client,colaborador)
				message_Soporte = (email_subject_Soporte, email_body_Soporte , 'as.estiloonline@gmail.com', ['soporte@apreciasoft.com'])
				#enviamos el correo
				send_mass_mail((message_colaborador, message_client, message_Soporte), fail_silently=False)
				mensaje = "Hemos Guardado sus datos de manera correcta"
				return render(request, 'Turn/NuevoTurno.html' , {'Form':Form ,'turnos':turnos ,'mensaje1':mensaje1, 'perfil':perfil, 'mensaje':mensaje})
			elif data == 1: # collaborador ocupado para esa hora y fecha
				mensaje1 = "El Colaborador que desea Contratar esta Ocupado Para El Dia y la hora deseado intente con otro collaborador o con otro dia"
				Form = TurnForm()
				fallido = "Tuvimos un error al cargar sus datos, verifiquelo e intente de nuevo"
		else:
				mensaje1 = "Errores en los datos Verifiquelos, y vuelva a intentarlo"
				Form = TurnForm()
				fallido = "Tuvimos un error al cargar sus datos, verifiquelo e intente de nuevo"
	return render(request, 'Turn/NuevoTurno.html' , {'Form':Form ,'turnos':turnos ,'mensaje1':mensaje1, 'perfil':perfil, 'fallido':fallido})

#edita los turnos en general
@login_required(login_url = 'Demo:login' )
def EditTurn(request , id_turn):
	TurnEditar = tb_turn.objects.get(id = id_turn)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	turnos = tb_turn.objects.filter(statusTurn__nameStatus="En Espera")
	perfil = result[0]
	fallido = None
	if request.method == 'GET':
		Form= TurnForm(instance=TurnEditar)
	else:
		Form= TurnForm(request.POST,instance=TurnEditar)
		if  Form.is_valid():
			turno 		 = Form.save(commit=False)
			turno.user = request.user
			turno.dateTurn = request.POST['TurnDate']
			turno.HoraTurn = request.POST['TimeTurn']
			turno.save()
			mensaje = "Guardamos sus datos de manera exitosa"
			return render (request, 'Turn/NuevoTurno.html', {'turnos':turnos,'Form':Form , 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'Turn/NuevoTurno.html', {'turnos':turnos,'Form':Form , 'perfil':perfil, 'fallido':fallido})

#edita los turnos en general
@login_required(login_url = 'Demo:login' )
def EditTurnList(request , id_turn):
	formulario = True
	turnos = tb_turn.objects.all().order_by('dateTurn')
	TurnEditar = tb_turn.objects.get(id = id_turn)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
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
			turno.isProcessClient = TurnEditar.isProcessClient
			turno.isProcessCollaborator = TurnEditar.isProcessCollaborator
			turno.save()
			return redirect ('Turnos:listTurnos')
	return render (request, 'Turn/ListaDeTurnos.html', {'TurnEditar':TurnEditar,'turnos':turnos,'Form':Form , 'perfil':perfil})




#borra los turnos
@login_required(login_url = 'Demo:login' )
def DeleteTurn(request , id_turn):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	TurnoBorrar = tb_turn.objects.get(id = id_turn)
	if request.method == 'POST':
		TurnoBorrar.delete()
		mensaje = "hemos borrado sus datos de manera exitosa"
		return render (request, 'Turn/DeleteTurno.html', {'TurnoBorrar':TurnoBorrar, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'Turn/DeleteTurno.html', {'TurnoBorrar':TurnoBorrar, 'perfil':perfil})