#josue gabriel}
#fevhs en Python

from datetime import date, time, datetime

#fechas actual
hoy = date.today()
print(hoy)

#formatear fecha

formateado = hoy.strftime("%d/%m/%Y")
print(formateado)


#hora actual
fecha_actual = datetime.now()
print(fecha_actual)

#capturar el año

anio = fecha_actual.year
print(anio)

mes = fecha_actual.month
print(mes)

dia =fecha_actual.day
print(dia)

hora_actual = fecha_actual.strftime("%H:%M:%S")
print(hora_actual)

#formato_AM_PM
hora_am_pm = fecha_actual.strftime("%I:%M:%S %p")
print(hora_am_pm)