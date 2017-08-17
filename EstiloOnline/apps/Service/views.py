from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Service.models import tb_service
from apps.Service.forms import ServiceForm
#datos para la vista principal arriba de las citas y los ingresos.
from django.db.models import Count, Min, Sum, Avg
from datetime import date 
from apps.Turn.models import tb_turn
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso
from apps.UserProfile.models import tb_profile
from apps.scripts.validatePerfil import validatePerfil


# Create your views here.
@login_required(login_url = 'Demo:login' )
def NuevoService(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = ServiceForm
	if request.method == 'POST':
		Form = ServiceForm(request.POST or None)
		if Form.is_valid():
			servicio = Form.save(commit=False)
			servicio.user = request.user
			servicio.save()
			return redirect('Servicios:listService')
		else:
			Form = ServiceForm()
	
	return render(request, 'Service/NuevoServicio.html' , {'Form':Form, 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def EditService(request, id_service):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	ServiceEditar= tb_service.objects.get(id=id_service)
	if request.method == 'GET':
		Form= ServiceForm(instance = ServiceEditar)
	else:
		Form = ServiceForm(request.POST, instance = ServiceEditar)
		if Form.is_valid():
			servicio = Form.save(commit=False)
			servicio.user = request.user
			servicio.save()
			return redirect ('Servicios:listService')
	return render (request, 'Service/NuevoServicio.html' , {'Form':Form, 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def DeleteService(request, id_service):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	serviceBorrar= tb_service.objects.get(id=id_service)
	if request.method == 'POST':
		serviceBorrar.delete()
		return redirect ('Servicios:listService')
	return render (request, 'Service/DeleteService.html', {'serviceBorrar':serviceBorrar, 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def listService(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Listado = tb_service.objects.all()

	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))

	context = {
	'perfil':perfil,
	'Listado':Listado,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,

	}
	return render (request, 'Service/ListServicio.html',context)

def Servicios(request):
	servicios = tb_service.objects.all()[:10]
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]

	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))

	context = {
	'perfil':perfil,
	'servicios':servicios,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,

	}
	return render(request, 'Service/servicios.html' , context )