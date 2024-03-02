#Alejandra Rodriguez Guevara 21310127 6E1

# -> TEMA: Modulo datetime para fechas
print("\n -> Fecha actual de la compu \n")#Explicamos lo que hara el codigo brevemente con un print

import datetime #Importabamos el modulo datetime

PCdate = datetime.datetime.now() #Mandamos a llamar con palabras reservadas la fecha actual
print(PCdate)#Imprimimos el dato que nos regresan

Mydate = datetime.datetime(2002,11,1,11,48) #Damos de alta la fecha que queremos que nos regrese
print(Mydate)#Imprimimos el dato que dimos de alta

# -> TEMA 2: Fechas con strftime()
import locale #Importamos el modulo locale el cual nos ayudara a poner las fechas en español
locale.setlocale(locale.LC_ALL, "es-ES")#Escribimos esta linea da codigo para que con el modulo que importamos se traduzcan las fechas
print("\n -> Formas de modifcar lo que recibimos por la computadora\n")#Explicamos lo que hara el codigo brevemente con un print
fechaalmomento = datetime.datetime.now()#Mandamos a llamar con palabras reservadas la fecha actual


print(fechaalmomento.strftime("Día de la semana en corto: %a "))#Como nos muestran en el curso, la clave reservada %a sirve para obtener el dia de la semana abreviado, y luego lo imprimomos para comprobar
print(fechaalmomento.strftime("Día de la semana full: %A "))#Como nos muestran en el curso, la clave reservada %A sirve para obtener el dia de la semana completo
print(fechaalmomento.strftime("Mes en corto: %b "))#Como nos muestran en el curso, la clave reservada %b sirve para obtener el mes abreviado
print(fechaalmomento.strftime("Mes full: %B "))#Como nos muestran en el curso, la clave reservada %B sirve para obtener el dia del mes completo
print(fechaalmomento.strftime("Fecha full: %c "))#Como nos muestran en el curso, la clave reservada %c sirve para obtener la fecha completa
print(fechaalmomento.strftime("Siglo: %C "))#Como nos muestran en el curso, la clave reservada %C sirve para obtener el siglo
print(fechaalmomento.strftime("Día del mes (01 - 31): %d "))#Como nos muestran en el curso, la clave reservada %d sirve para obtener el dia del mes empezando por 01 a 31
print(fechaalmomento.strftime("dia/mes/año: %D "))#Como nos muestran en el curso, la clave reservada %D sirve para obtener el dia/mes/año
print(fechaalmomento.strftime("Día del mes (1 - 31): %e "))#Como nos muestran en el curso, la clave reservada %e sirve para obtener el dia del mes empezando por 1 a 31
print(fechaalmomento.strftime("Año en dos dígitos: %g "))#Como nos muestran en el curso, la clave reservada %g sirve para obtener el año con dos digitos
print(fechaalmomento.strftime("Año en cuatro dígitos: %G "))#Como nos muestran en el curso, la clave reservada %G sirve para obtener el año con cuatro digitos
print(fechaalmomento.strftime("Mes abreviado: %h "))#Como nos muestran en el curso, la clave reservada %h sirve para obtener el mes abreviado
print(fechaalmomento.strftime("Hora format 24hrs: %H "))#Como nos muestran en el curso, la clave reservada %H sirve para obtener la hora con formato de 24 horas
print(fechaalmomento.strftime("Hora format 12hrs: %I "))#Como nos muestran en el curso, la clave reservada %I sirve para obtener la hora con formato de 12 horas
print(fechaalmomento.strftime("Día del año: %j "))#Como nos muestran en el curso, la clave reservada %j sirve para obtener el dia del año
print(fechaalmomento.strftime("Mes en numero: %m "))#Como nos muestran en el curso, la clave reservada %m sirve para obtener el mes en formato de numero
print(fechaalmomento.strftime("Minuto: %M "))#Como nos muestran en el curso, la clave reservada %M sirve para obtener en que minuto estamos de la hora
print(fechaalmomento.strftime("Salto de línea: %n"))#Como nos muestran en el curso, la clave reservada %n sirve para hacer un salto de linea
print(fechaalmomento.strftime("AM o PM: %p "))#Como nos muestran en el curso, la clave reservada %p sirve para obtener si la hora en la que estamos es AM o PM
print(fechaalmomento.strftime("Hora y (AM o PM): %r"))#Como nos muestran en el curso, la clave reservada %r sirve para obtener la hora actual y si es AM o PM
print(fechaalmomento.strftime("Hora y minutos: %R"))#Como nos muestran en el curso, la clave reservada %R sirve para obtener la hora actual con hora y minutos
print(fechaalmomento.strftime("Segundos: %S"))#Como nos muestran en el curso, la clave reservada %S sirve para obtener en que segundos estamos de la hora
print(fechaalmomento.strftime("Tabulación: %t Ajalas"))#Como nos muestran en el curso, la clave reservada %t sirve para hacer una tabulacion
print(fechaalmomento.strftime("Hora, minutos y segundos: %T"))#Como nos muestran en el curso, la clave reservada %T sirve para obtener la hora en formato, hora-minutos-segundos
print(fechaalmomento.strftime("Día de la semana en número: %u"))#Como nos muestran en el curso, la clave reservada %u sirve para obtener el dia de la semana en numero
print(fechaalmomento.strftime("Semana del año (empezando en domingo): %U"))#Como nos muestran en el curso, la clave reservada %U sirve para obtener en que semana del año estamos empezando por domingo
print(fechaalmomento.strftime("Semana del año(Condiciones especiales): %V"))#Como nos muestran en el curso, la clave reservada %V sirve para obtener en que semana del año estamos con condiciones especiales
print(fechaalmomento.strftime("Semana del año (empezando en lunes): %W"))#Como nos muestran en el curso, la clave reservada %W sirve para obtener en que semana del año estamos empezando por lunes
print(fechaalmomento.strftime("Día de la semana (empezando en domingo): %w"))#Como nos muestran en el curso, la clave reservada %w sirve para obtener el dia de la semana en numero empezando por domingo
print(fechaalmomento.strftime("Día/mes/año de dos dígitos: %x"))#Como nos muestran en el curso, la clave reservada %x sirve para obtener la fecha en dia/mes/año con dos digitos
print(fechaalmomento.strftime("Hora/minutos/segundos: %X"))#Como nos muestran en el curso, la clave reservada %X sirve para obtener la fecha en hora/minutos/segundos con dos digitos y si es AM o PM
print(fechaalmomento.strftime("Año corto: %y"))#Como nos muestran en el curso, la clave reservada %y sirve para obtener el año en dos digitos como con %g
print(fechaalmomento.strftime("Año largo: %Y"))#Como nos muestran en el curso, la clave reservada %Y sirve para obtener el año en cuatro digitos como con %G
