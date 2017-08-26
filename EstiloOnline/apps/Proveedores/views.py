from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Proveedores.models import tb_proveedor
from apps.Proveedores.forms import ProveedorForm
from apps.UserProfile.models import tb_profile
from apps.scripts.validatePerfil import validatePerfil

#datos para la vista principal arriba de las citas y los ingresos.
from django.db.models import Count, Min, Sum, Avg
from datetime import date 
from apps.Turn.models import tb_turn
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso
# enviar correos
from django.core.mail import send_mail
from django.core.mail import send_mass_mail

# Create your views here.
@login_required(login_url = 'Demo:login' )
def ListProveedores(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]

	proveedores = tb_proveedor.objects.all()
	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	context = {
	'perfil':perfil,
	'proveedores':proveedores,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,

	}


	return render (request, 'Proveedores/ListProveedores.html', context)


@login_required(login_url = 'Demo:login' )
def NuevoProveedor(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = ProveedorForm
	fallido = None
	if request.method == 'POST':
		Form = ProveedorForm(request.POST or None)
		if Form.is_valid():
			proveedor = Form.save(commit=False)
			proveedor.user = request.user
			proveedor.save()
			#mandar mensaje de nuevo usuario
			#Enviaremos los correos a el colaborador y al cliente 
			#cliente
			usuario = proveedor.email #trato de traer el colaborador del formulario
			email_subject_usuario = 'Estilo Online Nuevo Proveedor'
			email_body_usuario = "Hola %s, gracias por formar parte de nuestra familia como proveedor, toda tu informacion esta disponible aqui http://estiloonline.pythonanywhere.com" %(proveedor.nameProveedor)
			message_usuario = (email_subject_usuario, email_body_usuario , 'as.estiloonline@gmail.com', [usuario])
			#mensaje para apreciasoft
			email_subject_Soporte = 'Nuevo Proveedor Registrado'
			email_body_Soporte = "se ha registrado un nuevo proveedor satisfactoriamente con nombre %s para verificar ingrese aqui http://estiloonline.pythonanywhere.com" %(proveedor.nameProveedor)
			message_Soporte = (email_subject_Soporte, email_body_Soporte , 'as.estiloonline@gmail.com', ['soporte@apreciasoft.com'])
			#enviamos el correo
			send_mass_mail((message_usuario, message_Soporte), fail_silently=False)
			mensaje = "Hemos Guardado de manera exitosa su nuevo proveedor"
			return render(request, 'Proveedores/NuevoProveedor.html' , {'Form':Form, 'perfil':perfil, 'mensaje':mensaje})		
		else:
			Form = ProveedorForm()
			fallido = "No hemos podido guardar su nuevo proveedor, verifiquelo e intente de nuevo"
	return render(request, 'Proveedores/NuevoProveedor.html' , {'Form':Form, 'perfil':perfil, 'fallido':fallido})



@login_required(login_url = 'Demo:login' )
def EditarProveedor(request, id_proveedor):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	proveedorEditar= tb_proveedor.objects.get(id=id_proveedor)
	fallido = None
	if request.method == 'GET':
		Form= ProveedorForm(instance = proveedorEditar)
	else:
		Form = ProveedorForm(request.POST, instance = proveedorEditar)
		if Form.is_valid():
			proveedor = Form.save(commit=False)
			proveedor.user = request.user
			proveedor.save()
			mensaje = 'hemos guardado de manera exitosa tus nuevos datos'
			return render (request, 'Proveedores/NuevoProveedor.html' , {'Form':Form, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'Proveedores/NuevoProveedor.html' , {'Form':Form, 'perfil':perfil, 'fallido':fallido})


@login_required(login_url = 'Demo:login' )
def EliminarProveedor(request, id_proveedor):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	proveedorBorrar= tb_proveedor.objects.get(id=id_proveedor)
	fallido = None
	if request.method == 'POST':
		proveedorBorrar.delete()
		mensaje = 'Hemos Borrado manera exitosa todos sus registros'
		return render (request, 'Proveedores/DeteteProveedores.html', {'proveedorBorrar':proveedorBorrar, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'Proveedores/DeteteProveedores.html', {'proveedorBorrar':proveedorBorrar, 'perfil':perfil})