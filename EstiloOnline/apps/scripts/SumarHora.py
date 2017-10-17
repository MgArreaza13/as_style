# para usar timedelta hay que importarla
from datetime import datetime, timedelta
 
def sumar_hora(hora1,hora2):
    formato = "%H:%M"
    lista = hora2.split(":")
    hora=int(lista[0])
    minuto=int(lista[1])
    h1 = datetime.strptime(hora1, formato)
    dh = timedelta(hours=hora) 
    dm = timedelta(minutes=minuto)          
    resultado1 =h1 
    resultado2 = resultado1 + dm
    resultado = resultado2 + dh
    resultado=resultado.strftime(formato)

    return str(resultado)
 



