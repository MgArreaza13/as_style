from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso
from django.db.models import Count, Min, Sum, Avg
from apps.Caja.forms import IngresoForm
from apps.Caja.forms import EgresoForm
from django.http import HttpResponse
from apps.ReservasWeb.models import tb_reservasWeb
from apps.Configuracion.models import tb_formasDePago
from apps.Configuracion.models import tb_tipoIngreso
from apps.Turn.models import tb_turn
# Create your views here.
from apps.scripts.validatePerfil import validatePerfil

from apps.UserProfile.models import tb_profile



def NuevoPagoReservaOnline(request):
	status = 200
	id_reserva = request.GET.get('id_reserva', None)
	id_metodo_pago = request.GET.get('id_metodo_pago', None)
	id_monto = request.GET.get('id_monto', None)
	reserva = tb_reservasWeb.objects.get(id= id_reserva)
	reserva.montoPagado += float(id_monto)
	reserva.save()
	if reserva.montoAPagar == reserva.montoPagado:
		reserva.isPay = True
		reserva.save()
	ingreso = tb_ingreso()
	ingreso.user = request.user
	ingreso.reserva = reserva
	ingreso.tipoPago = tb_formasDePago.objects.get(id = id_metodo_pago )
	ingreso.tipoIngreso = tb_tipoIngreso.objects.get(id = 1)
	ingreso.service = reserva.servicioPrestar
	ingreso.monto = float(id_monto)
	ingreso.descripcion = 'Pago de Reserva Web'
	ingreso.save()
	return HttpResponse(status)




def NuevoPagoTurno(request):
	status = 200
	id_reserva = request.GET.get('id_reserva', None)
	id_metodo_pago = request.GET.get('id_metodo_pago', None)
	id_monto = request.GET.get('id_monto', None)
	turno = tb_turn.objects.get(id= id_reserva)
	turno.montoPagado += float(id_monto)
	turno.save()
	if turno.montoAPagar == turno.montoPagado:
		turno.isPay = True
		turno.save()
	ingreso = tb_ingreso()
	ingreso.user = request.user
	ingreso.turno = turno
	ingreso.tipoPago = tb_formasDePago.objects.get(id = id_metodo_pago )
	ingreso.tipoIngreso = tb_tipoIngreso.objects.get(id = 1)
	ingreso.service = turno.servicioPrestar
	ingreso.monto = float(id_monto)
	ingreso.descripcion = 'Pago de Turno Web'
	ingreso.save()
	return HttpResponse(status)







#########Ingresos##############








###############LISTADO PRINCIPAL DE LOS INGRESOS, MUESTRA LA TABLA DE INGRESOS################
@login_required(login_url = 'Demo:login' )
def IngresoList(request):
	ingresos = tb_ingreso.objects.all().order_by('id') # query para todo los ingresos
	total_ingresos = tb_ingreso.objects.all().aggregate(total=Sum('monto'))
	total_egresos  = tb_egreso.objects.all().aggregate(total=Sum('monto'))
	total_efectivo_caja = []
	total_pago_efectivo = tb_ingreso.objects.filter(tipoPago__nameFormasDePago='Efectivo').aggregate(total=Sum('monto'))
	total_pago_efectivo_egresos = tb_egreso.objects.filter(tipoPago__nameFormasDePago='Efectivo').aggregate(total=Sum('monto'))
	total_pago_tarjetas = tb_ingreso.objects.filter(tipoPago__nameFormasDePago='Tarjetas').aggregate(total=Sum('monto'))
	if total_pago_efectivo['total'] != None and total_pago_efectivo_egresos['total'] != None:
		total_efectivo_caja = total_pago_efectivo['total'] - total_pago_efectivo_egresos['total']
	elif total_pago_efectivo['total'] != None and total_pago_efectivo_egresos['total'] == None:
		total_efectivo_caja = total_pago_efectivo['total'] 
	else:
		total_efectivo_caja = None
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	context = {
	'perfil':perfil,
	'ingresos':ingresos,
	'total_efectivo_caja':total_efectivo_caja,
	'total_ingresos':total_ingresos,
	'total_egresos':total_egresos,
	'total_pago_efectivo':total_pago_efectivo,
	'total_pago_tarjetas':total_pago_tarjetas ,
	}
	return render(request, 'Caja/ResumenIngresos.html', context)


@login_required(login_url = 'Demo:login' )
def NuevoIngreso(request):
	Form = IngresoForm
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	fallido = None
	if request.method == 'POST':
		Form = IngresoForm(request.POST or None)
		if Form.is_valid():
			
			ingreso = Form.save(commit=False)
			ingreso.user = request.user
			if request.POST['descripcion'] == "":
				ingreso.descripcion = 'Sin Comentarios'
			else:
				ingreso.descripcion = request.POST['descripcion']
			ingreso.save()
			mensaje = 'Hemos Cargado Su ingreso de manera exitosa'
			return render(request, 'Caja/NuevoIngreso.html' , {'Form':Form, 'perfil':perfil, 'mensaje':mensaje})
		else:
			Form = IngresoForm()
			fallido = "Hemos tenido algun problema con sus datos, por eso no hemos procesado su ingreso, verifiquelo e intentelo de nuevo"
	return render(request, 'Caja/NuevoIngreso.html' , {'Form':Form, 'perfil':perfil, 'fallido':fallido})





#########Egresos##############


###############LISTADO PRINCIPAL DE LOS EGRESOS, MUESTRA LA TABLA DE EGRESOS################
@login_required(login_url = 'Demo:login' )
def EgresoList(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	egresos = tb_egreso.objects.all().order_by('id')
	total_ingresos = tb_ingreso.objects.all().aggregate(total=Sum('monto'))
	total_egresos  = tb_egreso.objects.all().aggregate(total=Sum('monto'))
	total_pago_efectivo = tb_ingreso.objects.filter(tipoPago__nameFormasDePago='Efectivo').aggregate(total=Sum('monto'))
	total_pago_efectivo_egresos = tb_egreso.objects.filter(tipoPago__nameFormasDePago='Efectivo').aggregate(total=Sum('monto'))
	total_pago_tarjetas = tb_ingreso.objects.filter(tipoPago__nameFormasDePago='Tarjetas').aggregate(total=Sum('monto'))
	total_efectivo_caja = []
	if total_pago_efectivo['total'] != None and total_pago_efectivo_egresos['total'] != None:
		total_efectivo_caja = total_pago_efectivo['total'] - total_pago_efectivo_egresos['total']
	elif total_pago_efectivo['total'] != None and total_pago_efectivo_egresos['total'] == None:
		total_efectivo_caja = total_pago_efectivo['total'] 
	else:
		total_efectivo_caja = None
	context = {
	'perfil':perfil,
	'egresos':egresos,
	'total_efectivo_caja':total_efectivo_caja,
	'total_ingresos':total_ingresos,
	'total_egresos':total_egresos,
	'total_pago_efectivo':total_pago_efectivo,
	'total_pago_tarjetas':total_pago_tarjetas ,
	}
	return render(request, 'Caja/ResumenEgresos.html',context)



@login_required(login_url = 'Demo:login' )
def NuevoEgreso(request):
	Form = EgresoForm
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	fallido = None
	if request.method == 'POST':
		Form = EgresoForm(request.POST or None)
		if Form.is_valid():
			egreso = Form.save(commit=False)
			egreso.user = request.user
			if request.POST['descripcion'] == "":
				egreso.descripcion = 'Sin Comentarios'
			else:
				egreso.descripcion = request.POST['descripcion']
			egreso.save()
			mensaje = 'Hemos Cargado Su egreso de manera exitosa'
			return render(request, 'Caja/NuevoEgreso.html' , {'Form':Form, 'perfil':perfil, 'mensaje':mensaje})

		else:
			Form = EgresoForm()
			fallido = "Hemos tenido algun problema con sus datos, por eso no hemos procesado su ingreso, verifiquelo e intentelo de nuevo"
	return render(request, 'Caja/NuevoEgreso.html' , {'Form':Form, 'perfil':perfil, 'fallido':fallido})