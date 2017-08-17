# Esta Funcion Tratara de validar el tipo de usuario.
# que si es None el usuario no tiene perfil , de lo contrario el usuario si tiene perfil 

#En esta funcione se le pasara el resultado de un queryset
#si el query viene vacio sera NONE por lo que se podra validar en el templete
#de lo contrario se imprimiran en el panel principal los datos del usuario que ingresa

def validatePerfil(x):
	if len(x) ==0:
		return [False]
	elif len(x) >= 1:
		return x
	else:
		return False
