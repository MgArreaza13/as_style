from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import date
from apps.ReservasWeb.models import tb_reservasWeb
from apps.Turn.models import tb_turn
from apps.ReservasWeb.forms import ReservasWebForm
from apps.Service.models import tb_service
from apps.Notificaciones.models import Notificacion
from apps.Configuracion.models import tb_turn_sesion
from apps.Product.models import tb_product
from apps.Client.models import tb_client_WEB
from apps.Collaborator.models  import tb_collaborator
from apps.Configuracion.models import tb_status
# enviar correos
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from datetime import date 
from django.http import HttpResponse
from django.core import serializers

def ReservaWebQueryset(request):
	print('funciono entro')
	date = request.GET.get('date', None)
	print(date)
	query = serializers.serialize("json", tb_reservasWeb.objects.filter(dateTurn = date).filter(statusTurn__nameStatus='Confirmada'))
	print(query)
	return HttpResponse(query)

def web(request):
	turnos = tb_turn.objects.filter(statusTurn__nameStatus="Confirmada")
	ReservasWeb = tb_reservasWeb.objects.filter(statusTurn__nameStatus="Confirmada")
	productos = tb_product.objects.all()
	servicios = tb_service.objects.all()
	colaboradores = tb_collaborator.objects.all()
	Form = ReservasWebForm
	notificacion = Notificacion()
	tipe_turnos = tb_turn_sesion.objects.all()
	user = tb_client_WEB()
	fallido = None
	if request.method == 'POST':
		Form = ReservasWebForm(request.POST or None)
		if Form.is_valid():
			print(request.POST)
			turno = Form.save(commit=False)
			turno.dateTurn = request.POST['FechaSeleccionada']
			turno.turn = tb_turn_sesion.objects.get(id=request.POST['TurnSeleccionado'])
			turno.statusTurn = tb_status.objects.get(nameStatus="Sin Aprobar")
			turno.servicioPrestar=tb_service.objects.get(id = request.POST['ServicioSeleccionado'])
			turno.montoAPagar = float(request.POST['total'])  
			turno.collaborator = tb_collaborator.objects.get(id = request.POST['ColaboradorSeleccionado'])
			if request.POST['ProductosSeleccionados'] != ' ':
				turno.description = request.POST['ProductosSeleccionados']
			else:
				turno.description = 'Sin Descripcion'
			print(turno.description)
			turno.save()
			notificacion.nombre = turno.nombre
			notificacion.dateTurn = turno.dateTurn
			notificacion.save()
			#creo el cliente web , debo validar si ya existe y agregar un contador
			query_set_user = tb_client_WEB.objects.filter(mail= turno.mail)
			if (len(query_set_user) == 1):
				print('entre en el condicional')
				query_set_user[0].numeroReservasWeb += 1
				query_set_user[0].save()
			else:
				user = tb_client_WEB()
				user.nombre = turno.nombre
				user.mail = turno.mail 
				user.telefono = turno.telefono
				user.save()
			turno_enviar = tb_reservasWeb.objects.get(id=turno.id)
			mensaje ="se ha registrado de forma correcta sus datos gracias por contactarnos"
			#mandar mensaje de nuevo usuario
			#Enviaremos los correos a el colaborador y al cliente 
			#cliente
			usuario = turno.mail #trato de traer el colaborador del formulario
			email_subject_usuario = 'Multipoint - Nueva Reserva'
			email_body_usuario = "Hola %s, gracias por solicitar una nueva reserva , para disfrutar de nuestros servicios te invitamos a resgistrarte aqui http://multipoint.pythonanywhere.com/" %(turno.nombre)
			message_usuario = (email_subject_usuario, email_body_usuario , 'as.estiloonline@gmail.com', [usuario])
			#mensaje para apreciasoft
			email_subject_Soporte = 'Multipoint - Nueva Reserva'
			email_body_Soporte = "se ha registrado una nueva reserva , nombre:%s . correo:%s, numero:%s , te invitamos a contactarla y luego a cambiar el status de la reserva en  http://multipoint.pythonanywhere.com/reservas/list/" %(turno.nombre, turno.mail, turno.telefono)
			message_Soporte = (email_subject_Soporte, email_body_Soporte , 'as.estiloonline@gmail.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com"])
			#enviamos el correo
			#send_mass_mail((message_usuario, message_Soporte), fail_silently=False)
			return redirect('/')
		else:
				fallido = "Errores en los datos Verifiquelos, y vuelva a intentarlo"
				Form = ReservasWebForm()
	return render(request, "ReservasWeb/reservasweb.html" , {'Form':Form, 'tipe_turnos':tipe_turnos ,'servicios':servicios,'productos':productos ,'ReservasWeb':ReservasWeb ,'turnos':turnos ,'fallido':fallido, 'colaboradores':colaboradores})

