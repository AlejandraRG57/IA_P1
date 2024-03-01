#Alejandra Rodriguez Guevara 21310127 6E1

# -> TEMA: Variables globales y locales
print("\n -> Declaracion y u so de variables globales y locales \n")#Explicamos lo que hara el codigo brevemente con un print

def prueba1(): #Creamos una funcion
    global var1 #Creamos una  variable global
    var1 = 1 #le damos un valor a la variable global

prueba1() #Mandamos a llamar a la funcion prueba1 para poder utilizar la variable global fuera de la funcion
print(var1)# Imprimimos la variable

def prueba2(): #Creamos una funcion
    global var2 #Creamos una  variable global
    var2 = 2 #le damos un valor a la variable global
    x= 3 #Creamos una variable local
    print(var2)# Imprimimos la variable dentro de la misma funcion
    print(x) #Imprimimos una variale local dentro de la funcion ya que afuera no se puede

prueba2()#Mandamos a llamar a la funcion prueba2

print("\n -> Anidacion en funciones con variables locales\n")#Explicamos lo que hara el codigo brevemente con un print

def prueba3(): #Creamos una funcion
    var4 = 4 #Declaramos una  variable global
    print(var4)
    
    def prueba4(): #La funcion prueba4 quedo anidada
        var3 = "Esto es cool?" #Declaramos una  variable global
        print(var3) #Imprimimos algo en la funcion prueba4
    prueba4()#Mandamos a llamar a la funcion prueba4
        
prueba3()#Mandamos a llamar a la funcion prueba3

# -> TEMA2: Funciones lambda
print("\n -> Funciones lambda -> Funciones con sitaxis reducida e importacion de modulos\n")#Explicamos lo que hara el codigo brevemente con un print

import math #Importamos el modulo math con el cual podremos usar diversas funciones matematicas en el codigo

def perimetrocircul(radio): #Declaramos una funcion para calcular el perimetro de un  circulo
	resultado =  2 * radio * math.pi #Ponemos la formula del perimetro del circulo y usamos el modulo math.pi para el valor de pi
	print(resultado) #Imprimimos el resultado

perimetrocircul(6)#Le damos un valor al radio de 6
