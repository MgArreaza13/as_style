from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.Product.models import tb_product
from apps.Product.forms import ProductForm

from apps.UserProfile.models import tb_profile
from apps.scripts.validatePerfil import validatePerfil
from django.http import JsonResponse

#datos para la vista principal arriba de las citas y los ingresos.
from django.db.models import Count, Min, Sum, Avg
from datetime import date 
from apps.Turn.models import tb_turn
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso




def ProductiDetail(request):
	id_producto = request.GET.get('id_producto', None)
	pro=tb_product.objects.filter(id=id_producto)
	producto = pro[0]
	data = {
        'value':producto.priceList,
        'nombre':producto.nameProduct,
        'descripcion':producto.descriptionProduct,

    }
	return JsonResponse(data)





@login_required(login_url = 'Demo:login' )
def pructosCliente(request):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	productos = tb_product.objects.all()
	return render(request, 'Product/productosdetalles.html' , {'perfil':perfil,'productos':productos} )





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
	if request.method == 'POST':
		Form = ProductForm(request.POST, request.FILES or None)
		if Form.is_valid():
			print(request.POST)
			producto = Form.save(commit=False)
			producto.user = request.user
			producto.save()
			return redirect('Productos:ListProductos')
		else:
			Form = ProductForm()
	return render(request, 'Product/NuevoProducto.html' , {'Form':Form, 'perfil':perfil})



@login_required(login_url = 'Demo:login' )
def EditarProducto(request, id_producto):
	productoEditar= tb_product.objects.get(id=id_producto)
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	if request.method == 'GET':
		Form= ProductForm(instance = productoEditar)
	else:
		Form = ProductForm(request.POST , request.FILES  ,  instance = productoEditar)
		if Form.is_valid():
			producto = Form.save(commit=False)
			producto.user = request.user
			producto.save()
			return redirect ('Productos:ListProductos')
	return render (request, 'Product/NuevoProducto.html' , {'Form':Form, 'perfil':perfil})


@login_required(login_url = 'Demo:login' )
def EliminarProducto(request, id_producto):
	result = validatePerfil(tb_profile.objects.filter(user=request.user))
	perfil = result[0]
	productoBorrar= tb_product.objects.get(id=id_producto)
	if request.method == 'POST':
		productoBorrar.delete()
		return redirect ('Productos:ListProductos')
	return render (request, 'Product/DeleteProduct.html', {'productoBorrar':productoBorrar, 'perfil':perfil})



#######################SERVICIOS##########################

from rest_framework import viewsets
from apps.Product.serializers import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
	queryset = tb_product.objects.all()
	serializer_class = ProductSerializer