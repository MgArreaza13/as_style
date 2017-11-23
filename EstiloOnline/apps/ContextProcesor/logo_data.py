from apps.Configuracion.models import tb_logo

def render_logo(request):
	logo = None
	query = tb_logo.objects.filter(id = 1)
	print(query)
	if len(query) != 0 :
		logo = query[0]
	print(logo)
	return {'logo':logo}