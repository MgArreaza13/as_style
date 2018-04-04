from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from apps.UserProfile.models import tb_profile
from django.contrib.auth.models import User
from celery import Celery
from celery import task
from EstiloOnline.celery import app
import time
import json
import logging



@app.task
def NuevoPerfilEmail(mailUser,nameUser ):
	#mandar mensaje de nuevo usuario
	#Enviaremos los correos a el colaborador y al cliente 
	#colaborador
	usuario = mailUser #trato de traer el colaborador del formulario
	email_subject_usuario = 'Estilo Online Nuevo Cliente'
	email_body_usuario = "Hola %s, gracias por crearte un nuevo perfil de cliente, ya puedes crear nuevos turnos y muchas cosas mas" %(nameUser)
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', [usuario])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Nuevo perfil de clientes Registrado'
	email_body_Soporte = "se ha registrado un nuevo perfil de cliente con nombre %s" %(nameUser)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', 'mg.arreaza.13@gmail.com'])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)

@app.task
def NuevoUsuarioEmail(mailUser,nameUser):
	#########################verificar los privilegios del correo porque es el correo que falla #######
	#print(mailUser)
	#print(nameUser)
	#mandar mensaje de nuevo usuario
	#Enviaremos los correos a el colaborador y al cliente 
	#colaborador
	usuario = mailUser #trato de traer el colaborador del formulario
	email_subject_usuario = 'Bienvenido a Estilo Online'
	email_body_usuario = "Hola %s, te damos una cordial bienvenida a nuestro sistema esperemos que tengas una experiencia agradable con nuestro sistema" %(nameUser)
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', [usuario])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Nuevo Usuario Registrado'
	email_body_Soporte = "se ha registrado un nuevo usuario de nombre %s " %(nameUser)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', 'mg.arreaza.13@gmail.com'])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)


@app.task
def PerfilDeUsuarioMail(mailUser,nameUser ):
	#mandar mensaje de nuevo usuario
	#Enviaremos los correos a el colaborador y al cliente 
	#cliente
	usuario = mailUser #trato de traer el colaborador del formulario
	email_subject_usuario = 'Estilo Online Nuevo Cliente'
	email_body_usuario = "Hola %s, gracias por crearte un nuevo perfil de cliente, ya puedes crear nuevos turnos y muchas cosas mas" %(nameUser)
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', [usuario])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Nuevo cliente Registrado'
	email_body_Soporte = "se ha registrado un nuevo perfil de cliente con nombre %s " %(nameUser)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', 'mg.arreaza.13@gmail.com'])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)
	


@app.task
def PerfilColaboradorMail(mailUser, nameUser):
	usuario = mailUser #trato de traer el colaborador del formulario
	email_subject_usuario = 'Estilo Online Nuevo Colaborador'
	email_body_usuario = "Hola %s, gracias por crearte un nuevo perfil colaborador , ya puedes crear nuevos turnos y muchas cosas" %(nameUser)
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', [usuario])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Nuevo Colaborador Registrado'
	email_body_Soporte = "se ha registrado un nuevo perfil de colaborador con nombre %s " %(nameUser)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com','mg.arreaza.13@gmail.com'])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)




@app.task
def ProveedorMail(email, nameProveedor):
	usuario = email #trato de traer el colaborador del formulario
	email_subject_usuario = 'Estilo Online Nuevo Proveedor'
	email_body_usuario = "Hola %s, gracias por formar parte de nuestra familia como proveedor" %(nameProveedor)
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', [usuario])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Nuevo Proveedor Registrado'
	email_body_Soporte = "se ha registrado un nuevo proveedor satisfactoriamente con nombre %s " %(nameProveedor)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', 'mg.arreaza.13@gmail.com'])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)




@app.task
def CorreoDePagoSucursalMail(mail,nombre, telefono):
	usuario = mail #trato de traer el colaborador del formulario
	email_subject_usuario = 'Estilo Online - Gracias Por Registrar su Reserva'
	email_body_usuario = "Hola %s, gracias por hacer tu reserva con nosotros te recordamos que debes concretar el pago en nuestra sucursal en las proxima 24 horas para camniar el status de tu reserva, muchas gracias " %(nombre)
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', [usuario])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Estilo Online - Nueva Reserva WEB Completada Y Proximamente pagada en sucursal'
	email_body_Soporte = "se ha registrado  una  nueva reserva , nombre:%s . correo:%s, numero:%s , te invitamos a contactarla y luego a cambiar el status de la reserva luego que se complete el pago en la sucursal" %(nombre, mail, telefono)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com"])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)


@app.task
def ReservaPorPagarMail(mail, nombre, telefono):
	usuario = mail #trato de traer el colaborador del formulario
	email_subject_usuario = 'Estilo Online - Gracias Por su Pago'
	email_body_usuario = "Hola %s, gracias por completar su pago de manera exitosa, esperemos disfrute nuestros servicios" %(nombre)
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', [usuario])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Estilo Online - Nueva Reserva WEB PAGADA'
	email_body_Soporte = "se ha registrado un Pago de una  reserva , nombre:%s . correo:%s, numero:%s , te invitamos a contactarla y luego a cambiar el status de la reserva" %(nombre, mail, telefono)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com"])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)



@app.task
def ReservaWebConfirmadaMail(mail,nombre):
	email_subject_usuario = 'Reserva confirmada, motor de pago enviado'
	email_body_usuario = "Hola ha confirmado la reserva sera enviado el motor de pago " 
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com"])
	mail = mail
	email_subject_Soporte = 'Estilo Online - Reserva Confirmada'
	email_body_Soporte = "hola %s, hemos confirmado tu reserva web te invitamos a procesar tu pago " %(nombre)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', [mail])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)



@app.task
def StattusChangeMAil(nombre, mail, telefono, servicioPrestar, montoAPagar):
	usuario = mail #trato de traer el colaborador del formulario
	email_subject_usuario = 'Estilo Online - Gracias Por su Pago'
	email_body_usuario = "Hola %s, gracias por completar su pago de manera exitosa, hemos aprobado su solicitud ya de servicio , esperemos disfrute nuestros servicios" %(nombre)
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', [usuario])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Estilo Online - Nueva Reserva WEB PAGADA'
	email_body_Soporte = "se ha registrado un Pago de una  reserva , nombre:%s . correo:%s, numero:%s , para un servicio %s, y un monto de $%s te invitamos a revisarla" %(nombre, mail, telefono, servicioPrestar, montoAPagar)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com"])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)


@app.task
def ReservaWebMail(nombre, mail, telefono):
	usuario = mail #trato de traer el colaborador del formulario
	email_subject_usuario = 'Estilo Online - Nueva Reserva'
	email_body_usuario = "Hola %s, gracias por solicitar una nueva reserva , para disfrutar de nuestros servicios " %(nombre)
	message_usuario = (email_subject_usuario, email_body_usuario , 'estilo@b7000615.ferozo.com', [usuario])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Estilo Online - Nueva Reserva'
	email_body_Soporte = "se ha registrado una nueva reserva , nombre:%s . correo:%s, numero:%s , te invitamos a contactarla y luego a cambiar el status de la reserva " %(nombre, mail, telefono)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', "mg.arreaza.13@gmail.com"])
	#enviamos el correo
	send_mass_mail((message_usuario, message_Soporte), fail_silently=False)
	



@app.task
def NuevoTurnoParaHoyMAil(colaborador, colaborador_mailUser , client , client_mailUser):
	email_subject_Colaborador = 'Nuevo Turno Solicitado Por Cliente'
	email_body_Colaborador = "Hola %s, El presente mensaje es para informarle que ha recibido una nueva solicitud para un turno si desea revisarla y confirmarla" %(colaborador)
	email_colaborador = colaborador_mailUser
	message_colaborador = (email_subject_Colaborador, email_body_Colaborador , 'estilo@b7000615.ferozo.com', [email_colaborador])
	
	email_subject_client = 'Nuevo Turno Solicitado'
	email_body_Client = "Hola %s, El presente mensaje es para informarle que se ha enviado una nueva solicitud para un turno si desea revisarla y confirmarla" %(client)
	email_client = client_mailUser
	message_client = (email_subject_client, email_body_Client, 'estilo@b7000615.ferozo.com', [email_client])
	#mensaje para apreciasoft
	email_subject_Soporte = 'Nuevo Turno Solicitado en Estilo Online'
	email_body_Soporte = "Hola, soporte Apreciasoft, El presente mensaje es para informarle que el cliente  %s ha enviado una nueva solicitud para de turno para el colaborador %s " %(client,colaborador)
	message_Soporte = (email_subject_Soporte, email_body_Soporte , 'estilo@b7000615.ferozo.com', ['soporte@apreciasoft.com', 'mg.arreaza.13@gmail.com'])
	#enviamos el correo
	send_mass_mail((message_colaborador, message_client, message_Soporte), fail_silently=False)
				