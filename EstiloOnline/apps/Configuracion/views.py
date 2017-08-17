from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#modelos
from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_tipoEgreso
from apps.Configuracion.models import tb_status
from apps.Configuracion.models import tb_tipoCollaborador
from apps.Configuracion.models import tb_tipoServicio
from apps.Configuracion.models import tb_tipoProducto
from apps.Configuracion.models import tb_tipoComision
from apps.Configuracion.models import tb_sucursales
from apps.Configuracion.models import tb_formasDePago
from apps.UserProfile.models import tb_profile
#forms
from apps.Configuracion.forms import tipoIngresoForm
from apps.Configuracion.forms import tipoEgresoForm
from apps.Configuracion.forms import tipoStatusForm
from apps.Configuracion.forms import tipoCollaboradorForm
from apps.Configuracion.forms import tipoServicioForm
from apps.Configuracion.forms import tipoProductoForm
from apps.Configuracion.forms import tipoComisionForm
from apps.Configuracion.forms import sucursalesForm
from apps.Configuracion.forms import formasDePagoForm

# Create your views here.


#datos para la vista principal arriba de las citas y los ingresos.
from django.db.models import Count, Min, Sum, Avg
from datetime import date 
from apps.Turn.models import tb_turn
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso

from apps.scripts.validatePerfil import validatePerfil

@login_required(login_url = 'Demo:login' )
def Configuracion(request):
	tipoDeIngreso 		=  	tb_tipoIngreso.objects.all()
	tipoDeEgreso  		=  	tb_tipoEgreso.objects.all()
	tipoDeServicio 		=  	tb_tipoServicio.objects.all()
	tipoDeProducto		=	tb_tipoProducto.objects.all()
	tipoDeComision		=	tb_tipoComision.objects.all()
	TipoDeCollaborador	=	tb_tipoCollaborador.objects.all()
	tipoDeStatus		=	tb_status.objects.all()
	sucursales 			=	tb_sucursales.objects.all()
	formasdepago 		= 	tb_formasDePago.objects.all()

	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]

	contexto = {
	'perfil':perfil,
	'TipoDeIngreso':tipoDeIngreso,
	'TipoDeEgreso':tipoDeEgreso,
	'tipoDeServicio':tipoDeServicio,
	'tipoDeProducto':tipoDeProducto,
	'tipoDeComision':tipoDeComision,
	'TipoDeCollaborador':TipoDeCollaborador,
	'tipoDeStatus':tipoDeStatus,
	'sucursales':sucursales,
	'formasdepago':formasdepago,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,
	}
	return render(request, 'Configuracion/configuracion.html', contexto)




#Ingresos
@login_required(login_url = 'Demo:login' )
def NuevoTipoIngreso(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = tipoIngresoForm
	if request.method == 'POST':
		Form = tipoIngresoForm(request.POST or None)
		if Form.is_valid():
			TipoIngreso = Form.save(commit=False)
			TipoIngreso.user = request.user
			TipoIngreso.save()
			return redirect('Configuracion:Configuracion')
		else:
			Form = tipoIngresoForm()
	return render(request, 'Configuracion/NuevoTipoDeIngreso.html' , {'Form':Form, 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def EditarTipoIngreso(request, id_tipoIngreso):
	TipoIngresoEditar= tb_tipoIngreso.objects.get(id=id_tipoIngreso)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'GET':
		Form= tipoIngresoForm(instance = TipoIngresoEditar)
	else:
		Form = tipoIngresoForm(request.POST, instance = TipoIngresoEditar)
		if Form.is_valid():
			TipoIngreso = Form.save(commit=False)
			TipoIngreso.user = request.user
			TipoIngreso.save()
			return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/NuevoTipoDeIngreso.html' , {'Form':Form, 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def BorrarTipoIngreso(request, id_tipoIngreso):
	tipoIngresoBorrar= tb_tipoIngreso.objects.get(id=id_tipoIngreso)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'POST':
		tipoIngresoBorrar.delete()
		return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/DeleteTipoIngreso.html', {'tipoIngresoBorrar':tipoIngresoBorrar, 'perfil':perfil})



#Egresos
@login_required(login_url = 'Demo:login' )
def NuevoTipoEgreso(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = tipoEgresoForm
	if request.method == 'POST':
		Form = tipoEgresoForm(request.POST or None)
		if Form.is_valid():
			TipoEgreso = Form.save(commit=False)
			TipoEgreso.user = request.user
			TipoEgreso.save()
			return redirect('Configuracion:Configuracion')
		else:
			Form = tipoEgresoForm()
	return render(request, 'Configuracion/NuevoTipoDeEgreso.html' , {'Form':Form, 'perfil':perfil})


@login_required(login_url = 'Demo:login' )
def EditarTipoEgreso(request, id_tipoEgreso):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	TipoEgresoEditar= tb_tipoEgreso.objects.get(id=id_tipoEgreso)
	if request.method == 'GET':
		Form= tipoEgresoForm(instance = TipoEgresoEditar)
	else:
		Form = tipoEgresoForm(request.POST, instance = TipoEgresoEditar)
		if Form.is_valid():
			TipoEgreso = Form.save(commit=False)
			TipoEgreso.user = request.user
			TipoEgreso.save()
			return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/NuevoTipoDeEgreso.html' , {'Form':Form, 'perfil':perfil})


@login_required(login_url = 'Demo:login' )
def BorrarTipoEgreso(request, id_tipoEgreso):
	TipoEgresoBorrar= tb_tipoEgreso.objects.get(id=id_tipoEgreso)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'POST':
		TipoEgresoBorrar.delete()
		return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/DeleteTipoEgreso.html', {'TipoEgresoBorrar':TipoEgresoBorrar, 'perfil':perfil})






#Status
@login_required(login_url = 'Demo:login' )
def NuevoStatus(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = tipoStatusForm
	if request.method == 'POST':
		Form = tipoStatusForm(request.POST or None)
		if Form.is_valid():
			Status = Form.save(commit=False)
			Status.user = request.user
			Status.save()
			return redirect('Configuracion:Configuracion')
		else:
			Form = tipoStatusForm()
	return render(request, 'Configuracion/NuevoStatus.html' , {'Form':Form, 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def EditarStatus(request, id_status):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	StatusEditar= tb_status.objects.get(id=id_status)
	if request.method == 'GET':
		Form= tipoStatusForm(instance = StatusEditar)
	else:
		Form = tipoStatusForm(request.POST, instance = StatusEditar)
		if Form.is_valid():
			Status = Form.save(commit=False)
			Status.user = request.user
			Status.save()
			return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/NuevoStatus.html' , {'Form':Form , 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def BorrarStatus(request, id_status):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	StatusBorrar= tb_status.objects.get(id=id_status)
	if request.method == 'POST':
		StatusBorrar.delete()
		return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/DeleteStatus.html', {'StatusBorrar':StatusBorrar, 'perfil':perfil})




#Collaborador
@login_required(login_url = 'Demo:login' )
def NuevoTipoCollaborador(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = tipoCollaboradorForm
	if request.method == 'POST':
		Form = tipoCollaboradorForm(request.POST or None)
		if Form.is_valid():
			TipoCollaborador = Form.save(commit=False)
			TipoCollaborador.user = request.user
			TipoCollaborador.save()
			return redirect('Configuracion:Configuracion')
		else:
			Form = tipoCollaboradorForm()
	return render(request, 'Configuracion/NuevoTipoDeCollaborador.html' , {'Form':Form , 'perfil':perfil})


@login_required(login_url = 'Demo:login' )
def EditarTipoCollaborador(request, id_TipoCollaborador):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	TipoCollaborador= tb_tipoCollaborador.objects.get(id=id_TipoCollaborador)
	if request.method == 'GET':
		Form= tipoCollaboradorForm(instance = TipoCollaborador)
	else:
		Form = tipoCollaboradorForm(request.POST, instance = TipoCollaborador)
		if Form.is_valid():
			collaborador = Form.save(commit=False)
			collaborador.user = request.user
			collaborador.save()
			return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/NuevoTipoDeCollaborador.html' , {'Form':Form, 'perfil':perfil})


@login_required(login_url = 'Demo:login' )
def BorrarTipoCollaborador(request, id_TipoCollaborador):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	TipoCollaboradorBorrar= tb_tipoCollaborador.objects.get(id=id_TipoCollaborador)
	if request.method == 'POST':
		TipoCollaboradorBorrar.delete()
		return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/DeleteTipoCollaborador.html', {'TipoCollaboradorBorrar':TipoCollaboradorBorrar, 'perfil':perfil})


#Servicios
@login_required(login_url = 'Demo:login' )
def NuevoTipoServicio(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = tipoServicioForm
	if request.method == 'POST':
		Form = tipoServicioForm(request.POST or None)
		if Form.is_valid():
			TipoServicio = Form.save(commit=False)
			TipoServicio.user = request.user
			TipoServicio.save()
			return redirect('Configuracion:Configuracion')
		else:
			Form = tipoServicioForm()
	return render(request, 'Configuracion/NuevoTipoDeServicio.html' , {'Form':Form, 'perfil':perfil})

@login_required(login_url = 'Demo:login' )
def EditarTipoServicio(request, id_TipoServicio):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	TipoServicio= tb_tipoServicio.objects.get(id=id_TipoServicio)
	if request.method == 'GET':
		Form= tipoServicioForm(instance = TipoServicio)
	else:
		Form = tipoServicioForm(request.POST, instance = TipoServicio)
		if Form.is_valid():
			TipoServicio = Form.save(commit=False)
			TipoServicio.user = request.user
			TipoServicio.save()
			return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/NuevoTipoDeServicio.html' , {'Form':Form, 'perfil':perfil})

@login_required(login_url = 'Demo:login' )
def BorrarTipoServicio(request, id_TipoServicio):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	TipoServicioBorrar= tb_tipoServicio.objects.get(id=id_TipoServicio)
	if request.method == 'POST':
		TipoServicioBorrar.delete()
		return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/DeleteTipoServicio.html', {'TipoServicioBorrar':TipoServicioBorrar, 'perfil':perfil})



#Productos
@login_required(login_url = 'Demo:login' )
def NuevoTipoProducto(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = tipoProductoForm
	if request.method == 'POST':
		Form = tipoProductoForm(request.POST or None)
		if Form.is_valid():
			TipoProducto = Form.save(commit=False)
			TipoProducto.user = request.user
			TipoProducto.save()
			return redirect('Configuracion:Configuracion')
		else:
			Form = tipoProductoForm()
	return render(request, 'Configuracion/NuevoTipoDeProducto.html' , {'Form':Form , 'perfil':perfil})

@login_required(login_url = 'Demo:login' )
def EditarTipoProducto(request, id_TipoProducto):
	TipoProducto= tb_tipoProducto.objects.get(id=id_TipoProducto)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'GET':
		Form= tipoProductoForm(instance = TipoProducto)
	else:
		Form = tipoProductoForm(request.POST, instance = TipoProducto)
		if Form.is_valid():
			tipoProducto = Form.save(commit=False)
			tipoProducto.user = request.user
			tipoProducto.save()
			return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/NuevoTipoDeProducto.html' , {'Form':Form, 'perfil':perfil})

@login_required(login_url = 'Demo:login' )
def BorrarTipoProducto(request, id_TipoProducto ):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	TipoProductoBorrar= tb_tipoProducto.objects.get(id=id_TipoProducto)
	if request.method == 'POST':
		TipoProductoBorrar.delete()
		return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/DeleteTipoProducto.html', {'TipoProductoBorrar':TipoProductoBorrar, 'perfil':perfil})




#Comision
@login_required(login_url = 'Demo:login' )
def NuevoTipoComision(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = tipoComisionForm
	if request.method == 'POST':
		Form = tipoComisionForm(request.POST or None)
		if Form.is_valid():
			TipoProducto = Form.save(commit=False)
			TipoProducto.user = request.user
			TipoProducto.save()
			return redirect('Configuracion:Configuracion')
		else:
			Form = tipoComisionForm()
	return render(request, 'Configuracion/NuevoTipoDeComision.html' , {'Form':Form, 'perfil':perfil})

@login_required(login_url = 'Demo:login' )
def EditarTipoComision(request, id_TipoComision):
	TipoComision= tb_tipoComision.objects.get(id=id_TipoComision)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'GET':
		Form= tipoComisionForm(instance = TipoComision)
	else:
		Form = tipoComisionForm(request.POST, instance = TipoComision)
		if Form.is_valid():
			tipoComision = Form.save(commit=False)
			tipoComision.user = request.user
			tipoComision.save()
			return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/NuevoTipoDeComision.html' , {'Form':Form, 'perfil':perfil})

@login_required(login_url = 'Demo:login' )
def BorrarTipoComision(request,id_TipoComision ):
	TipoComisionBorrar= tb_tipoComision.objects.get(id=id_TipoComision)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'POST':
		TipoComisionBorrar.delete()
		return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/DeleteTipoComision.html', {'TipoComisionBorrar':TipoComisionBorrar, 'perfil':perfil})



#sucursales 
@login_required(login_url = 'Demo:login' )
def nuevaSucursal(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = sucursalesForm
	if request.method == 'POST':
		Form = sucursalesForm(request.POST or None)
		if Form.is_valid():
			sucursal = Form.save(commit=False)
			sucursal.user = request.user
			sucursal.save()
			return redirect('Configuracion:Configuracion')
		else:
			Form = sucursalesForm()
	return render(request, 'Configuracion/NuevaSucursal.html' , {'Form':Form, 'perfil':perfil})


@login_required(login_url = 'Demo:login' )
def EditarSucursal(request, id_Sucursal):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	SucursalEditar= tb_sucursales.objects.get(id=id_Sucursal)
	if request.method == 'GET':
		Form= sucursalesForm(instance = SucursalEditar)
	else:
		Form = sucursalesForm(request.POST, instance = SucursalEditar)
		if Form.is_valid():
			sucursal = Form.save(commit=False)
			sucursal.user = request.user
			sucursal.save()
			return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/NuevaSucursal.html' , {'Form':Form, 'perfil':perfil})
@login_required(login_url = 'Demo:login' )


def BorrarSucursal(request , id_Sucursal):
	SucursalBorrar= tb_sucursales.objects.get(id=id_Sucursal)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'POST':
		SucursalBorrar.delete()
		return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/DeleteSucursal.html', {'SucursalBorrar':SucursalBorrar, 'perfil':perfil})



#formas de pago
@login_required(login_url = 'Demo:login' )
def nuevaFormaDePago(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = formasDePagoForm
	if request.method == 'POST':
		Form = formasDePagoForm(request.POST or None)
		if Form.is_valid():
			formadepago = Form.save(commit=False)
			formadepago.user = request.user
			formadepago.save()
			return redirect('Configuracion:Configuracion')
		else:
			Form = formasDePagoForm()
	return render(request, 'Configuracion/NuevoFormaDePago.html' , {'Form':Form, 'perfil':perfil})


@login_required(login_url = 'Demo:login' )
def EditarFormaDePago(request, id_FormaDePago):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	SucursalEditar= tb_formasDePago.objects.get(id=id_FormaDePago)
	if request.method == 'GET':
		Form= formasDePagoForm(instance = SucursalEditar)
	else:
		Form = formasDePagoForm(request.POST, instance = SucursalEditar)
		if Form.is_valid():
			formasdepago = Form.save(commit=False)
			formasdepago.user = request.user
			formasdepago.save()
			return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/NuevoFormaDePago.html' , {'Form':Form, 'perfil':perfil})

@login_required(login_url = 'Demo:login' )
def BorrarFormaDePago(request , id_FormaDePago):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	FormadePagoBorrar= tb_formasDePago.objects.get(id=id_FormaDePago)
	if request.method == 'POST':
		FormadePagoBorrar.delete()
		return redirect ('Configuracion:Configuracion')
	return render (request, 'Configuracion/DeleteFormaDePago.html', {'FormadePagoBorrar':FormadePagoBorrar, 'perfil':perfil})
