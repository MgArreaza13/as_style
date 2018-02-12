from django.contrib import admin
from apps.Caja.models import tb_ingreso
from apps.Caja.models import tb_egreso
from apps.Caja.models import tb_ingreso_manual
# Register your models here.


admin.site.register(tb_ingreso)
admin.site.register(tb_ingreso_manual)
admin.site.register(tb_egreso)
