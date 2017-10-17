from django.shortcuts import render, HttpResponse
from apps.Notificaciones.models import Notificacion
from apps.Notificaciones.serializers import NotiticacionSerializer
# Create your views here.
from django.http import JsonResponse
from django.core import serializers
from django.http import JsonResponse

def NotificacionesView(request):
	queryset = Notificacion.objects.filter(leida=False)
	serialized = serializers.serialize("json", queryset, fields=('dateTurn', 'HoraTurn', 'nombre'))
	return HttpResponse(serialized, content_type='application/json')



def NotificacionVista(request):
	
	pk = request.GET.get('pk', None)
	
	query = Notificacion.objects.get(id=pk)
	query.leida = True
	query.save()
	data = {
		'nombre':query.nombre,
		'hora':query.HoraTurn,
		'fecha':query.dateTurn
	}
	return JsonResponse(data)

#########################SERVICIOS@#####################

from rest_framework import viewsets


class NotificacionViewsets(viewsets.ModelViewSet):
	queryset = Notificacion.objects.filter(leida=False)
	serializer_class = NotiticacionSerializer