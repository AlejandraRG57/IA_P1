#Alejandra Rodriguez Guevara 21310127 6E1

# -> Condicional If Else

var1 = 7 #Planteamos esta primera variable para todas nuestras comparaciones
var2 = 55 #Planteamos esta segunda variable tambien para todas nuestras comparaciones
var3 = 21 #Planteamos esta tercera variable tambien para todas nuestras comparaciones

#Este es un ejemplo en el que se cumple la condicion
if var2 >= 35: #Comparamos si el numero es mayor o igual a 35
    print("Pasele señor")#Si cumple las condiciones imprime esto
else: #Si no cumple la condicion se pasaria al else
    print("Pasele jovenazo")#Se imprime esto en caso de no cumplirse la condicion

#Este es un ejemplo en el que no se cumple la condicion
if var3 >= 35: #Comparamos si el numero es mayor o igual a 35
    print("Pasele señor")#Si cumple las condiciones imprime esto
else: #Si no cumple la condicion se pasaria al else
    print("Pasele jovenazo")#Se imprime esto en caso de no cumplirse la condicion

# -> Condicional If Elif Else y uso de input()

credencial = int(input("¿Cual es su edad para crearle una credencial?\n"))#Planteamos una prengunta para que el usuario digite su respuesta
if credencial >= 1 and credencial <= 17: #Planteamos condiciones para entrar a el if
    print("Tome su identificacion infantil <3")#Si entraron a el if esta seria la respuesta
elif credencial >= 18 and credencial <= 59:#Planteamos condiciones para entrar a el elif, aqui se irian si no entraron a el anterior
    print("Tome su credencial del INE <3")#Si entraron a este elif esta seria la respuesta
elif credencial >= 60 and credencial <=99:#Planteamos condiciones para entrar a el elif, aqui se irian si no entraron a el anterior
    print("Tome su credencial del INAPAM <3")#Si entraron a este elif esta seria la respuesta
elif credencial == 0:#Planteamos condiciones para entrar a el elif, aqui se irian si no entraron a el anterior
    print("Ajalas, ¿Apenas naciste? que bello vuelve cuando tengas al menos un año")#Si entraron a este elif esta seria la respuesta
elif credencial >=100:#Planteamos condiciones para entrar a el elif, aqui se irian si no entraron a el anterior
    print("Tu ya viviste bro, no se que mas te podria dar, ¿cuando nacio chabelo?")#Si entraron a este elif esta seria la respuesta
else:#Planteamos condiciones para entrar a el else, aqui se irian si no entraron ninguno de los anteriores
    print("Eso no es una edad bro, vuelve cuando te acuerdes de tu edad")#Si no entraron a ninuna anterior el else les imprimiria esto
                
 
