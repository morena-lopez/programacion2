import locale

locale.setlocale(locale.LC_TIME,"es_ES.UTF-8")

from datetime import datetime

fecha_nac=input("ingrese su fecha de nacimiento (Formato:DD/MM/AAAA): ")

fecha_estructura=datetime.strptime(fecha_nac,"%d/%m/%Y")

dia=datetime.now()

diferencia=dia -fecha_estructura
print("Su edad en días es de ",diferencia.days," días desde tu nacimiento")

import time

fecha_est=time.strptime(fecha_nac,"%d/%m/%Y")
fecha_leg=time.strftime("%d de %B de %Y",fecha_est)
print("Su fecha de nacimiento es : ",fecha_leg)
