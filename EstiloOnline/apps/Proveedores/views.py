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
	if request.method == 'POST':
		Form = ProveedorForm(request.POST or None)
		if Form.is_valid():
			proveedor = Form.save(commit=False)
			proveedor.user = request.user
			proveedor.save()
			return redirect('Proveedores:ListProveedores')
		else:
			Form = ProveedorForm()
	return render(request, 'Proveedores/NuevoProveedor.html' , {'Form':Form, 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def EditarProveedor(request, id_proveedor):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	proveedorEditar= tb_proveedor.objects.get(id=id_proveedor)
	if request.method == 'GET':
		Form= ProveedorForm(instance = proveedorEditar)
	else:
		Form = ProveedorForm(request.POST, instance = proveedorEditar)
		if Form.is_valid():
			proveedor = Form.save(commit=False)
			proveedor.user = request.user
			proveedor.save()
			return redirect ('Proveedores:ListProveedores')
	return render (request, 'Proveedores/NuevoProveedor.html' , {'Form':Form, 'perfil':perfil})


@login_required(login_url = 'Demo:login' )
def EliminarProveedor(request, id_proveedor):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	proveedorBorrar= tb_proveedor.objects.get(id=id_proveedor)
	if request.method == 'POST':
		proveedorBorrar.delete()
		return redirect ('Proveedores:ListProveedores')
	return render (request, 'Proveedores/DeteteProveedores.html', {'proveedorBorrar':proveedorBorrar, 'perfil':perfil})