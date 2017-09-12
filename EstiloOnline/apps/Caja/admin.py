from django.contrib import admin
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso
from apps.Caja.models import tb_ingresoTurn
# Register your models here.


admin.site.register(tb_ingreso)
admin.site.register(tb_ingresoTurn)
admin.site.register(tb_egreso)