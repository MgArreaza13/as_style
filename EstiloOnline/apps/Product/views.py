from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Product.models import tb_product
from apps.Product.forms import ProductForm

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
def ListProductos(request):
	productos = tb_product.objects.all()
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]


	#queryset 
	turnos_hoy =  tb_turn.objects.filter(dateTurn=date.today()).filter(statusTurn__nameStatus='En Espera').count()
	ingresos_hoy = tb_ingreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))
	egresos_hoy  = tb_egreso.objects.filter(dateCreate=date.today()).aggregate(total=Sum('monto'))


	context = {
	'perfil':perfil,
	'productos':productos,
	'turnos_hoy':turnos_hoy,
	'ingresos_hoy':ingresos_hoy,
	'egresos_hoy':egresos_hoy,


	}
	return render (request, 'Product/ListProducts.html', context)


@login_required(login_url = 'Demo:login' )
def NuevoProducto(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	Form = ProductForm
	fallido = None
	if request.method == 'POST':
		Form = ProductForm(request.POST or None)
		if Form.is_valid():
			producto = Form.save(commit=False)
			producto.user = request.user
			producto.save()
			mensaje = "Hemos cargado de manera exitosa su nuevo Producto"
			return render(request, 'Product/NuevoProducto.html' , {'Form':Form, 'perfil':perfil, 'mensaje':mensaje})
		else:
			Form = ProductForm()
			fallid0 = "Hemos tenido problema al registrar sus datos, verifiquelos e intente nuevamente"
	return render(request, 'Product/NuevoProducto.html' , {'Form':Form, 'perfil':perfil, 'falido': fallido})



@login_required(login_url = 'Demo:login' )
def EditarProducto(request, id_producto):
	productoEditar= tb_product.objects.get(id=id_producto)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	fallido = None
	if request.method == 'GET':
		Form= ProductForm(instance = productoEditar)
	else:
		Form = ProductForm(request.POST, instance = productoEditar)
		if Form.is_valid():
			producto = Form.save(commit=False)
			producto.user = request.user
			producto.save()
			mensaje = "Hemos guardado correctamente sus nuevos datos"
			return render (request, 'Product/NuevoProducto.html' , {'Form':Form, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'Product/NuevoProducto.html' , {'Form':Form, 'perfil':perfil, 'fallido':fallido})


@login_required(login_url = 'Demo:login' )
def EliminarProducto(request, id_producto):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	productoBorrar= tb_product.objects.get(id=id_producto)
	fallido = None
	if request.method == 'POST':
		productoBorrar.delete()
		mensaje = 'Hemos Borrado Correctamente sus datos'
		return render (request, 'Product/DeleteProduct.html', {'productoBorrar':productoBorrar, 'perfil':perfil, 'mensaje':mensaje})
	return render (request, 'Product/DeleteProduct.html', {'productoBorrar':productoBorrar, 'perfil':perfil})
