from django.contrib import admin
from apps.Client.models import tb_client,tb_type_client,tb_liquidation_client_header,tb_invoicer_header_client

# Register your models here.

admin.site.register(tb_client)
admin.site.register(tb_type_client)
admin.site.register(tb_liquidation_client_header)
admin.site.register(tb_invoicer_header_client)