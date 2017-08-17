from django.contrib import admin
from apps.Configuracion.models import tb_tipoIngreso
from apps.Configuracion.models import tb_tipoEgreso
from apps.Configuracion.models import tb_tipoServicio
from apps.Configuracion.models import tb_tipoProducto
from apps.Configuracion.models import tb_tipoComision
from apps.Configuracion.models import tb_tipoCollaborador
from apps.Configuracion.models import tb_status
from apps.Configuracion.models import tb_sucursales
from apps.Configuracion.models import tb_formasDePago

# Register your models here.


admin.site.register(tb_tipoIngreso)
admin.site.register(tb_tipoEgreso)
admin.site.register(tb_tipoServicio)
admin.site.register(tb_tipoProducto)
admin.site.register(tb_tipoComision)
admin.site.register(tb_tipoCollaborador)
admin.site.register(tb_status)
admin.site.register(tb_sucursales)
admin.site.register(tb_formasDePago)