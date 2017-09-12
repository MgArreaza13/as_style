from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_ingresoTurn
from apps.Caja.models import tb_egreso
from django.db.models import Count, Min, Sum, Avg
from apps.Caja.forms import IngresoForm
from apps.Caja.forms import IngresoTurnForm
from apps.Caja.forms import EgresoForm
from apps.Turn.models import tb_turn
from apps.Collaborator.models import tb_collaborator
# Create your views here.
from apps.scripts.validatePerfil import validatePerfil

from apps.UserProfile.models import tb_profile

#########Ingresos##############

###############LISTADO PRINCIPAL DE LOS INGRESOS, MUESTRA LA TABLA DE INGRESOS################
@login_required(login_url = 'Demo:login' )
def IngresoList(request):
	total_ingresos =[]
	ingresos = tb_ingreso.objects.all().order_by('id') # query para todo los ingresos
	total_ingresos_normal = tb_ingreso.objects.all().aggregate(total=Sum('monto'))
	total_ingresos_turn	 = tb_ingresoTurn.objects.all().aggregate(total=Sum('monto'))
	total_ingresos = total_ingresos_normal['total'] + total_ingresos_turn['total']
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
def IngresoTurnList(request):
	ingresos = tb_ingresoTurn.objects.all().order_by('id') # query para todo los ingresos
	total_ingresos_normal = tb_ingreso.objects.all().aggregate(total=Sum('monto'))
	total_ingresos =[]
	total_ingresos_turn	 = tb_ingresoTurn.objects.all().aggregate(total=Sum('monto'))
	total_ingresos = total_ingresos_normal['total'] + total_ingresos_turn['total']
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
	return render(request, 'Caja/ResumenIngresosTurn.html', context)

@login_required(login_url = 'Demo:login' )
def NuevoIngreso(request):
	Form = IngresoForm
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	fallido = None
	if request.method == 'POST':
		Form = IngresoForm(request.POST or None)
		if Form.is_valid():
			print(request.POST)
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


@login_required(login_url = 'Demo:login' )
def NuevoIngresoTurn(request, id_turn):
	Form = IngresoTurnForm
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	turno  = tb_turn.objects.get(id=id_turn)
	fallido = None
	if request.method == 'POST':
		Form = IngresoTurnForm(request.POST or None)
		if Form.is_valid():
			ingreso = Form.save(commit=False)
			ingreso.user = request.user
			if request.POST['descripcion'] == "":
				ingreso.descripcion = 'Sin Comentarios'
			else:
				ingreso.descripcion = request.POST['descripcion']
			ingreso.turn = turno
			ingreso.save()
			turno.isPay = True
			colaborador =  tb_collaborator.objects.get(id= turno.collaborator.id)
			if colaborador.Typecomision == 'Porcentaje' :
				colaborador.MontoAcumulado += (colaborador.comision / 100 ) * ingreso.monto
			elif colaborador.Typecomision == 'Monto':
				colaborador.MontoAcumulado += colaborador.comision
			turno.save()
			colaborador.save()
			mensaje = 'Hemos Cargado Su ingreso de manera exitosa'
			return render(request, 'Caja/NuevoIngreso.html' , {'Form':Form, 'turno':turno, 'perfil':perfil, 'mensaje':mensaje})
		else:
			Form = IngresoTurnForm()
			fallido = "Hemos tenido algun problema con sus datos, por eso no hemos procesado su ingreso, verifiquelo e intentelo de nuevo"
	return render(request, 'Caja/NuevoIngreso.html' , {'Form':Form,'turno':turno, 'perfil':perfil, 'fallido':fallido})





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