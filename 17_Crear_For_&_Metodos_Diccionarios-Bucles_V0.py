#Alejandra Rodriguez Guevara 21310127 6E1 

# -> TEMA: Diccionarios

vengador1 = { #Declaramos un diccionario y sus variables
    "Nombre": "Black Widow",
    "Habilidad": "Experta en combate",
    "Estado": "QEPD"
    }

vengador2 = { #Declaramos un segundo diccionario y sus variables
    "Nombre":"Hulk",
    "Habilidad":"Mounstro gigante por radiacion",
    "Estado":"Vivo"
    }

vengador3 = { #Declaramos un tercer diccionario y sus variables
    "Nombre":"Iron Man",
    "Habilidad":"Genio, filantropo, millonario",
    "Estado":"QEPD"
    }

print("\n -> Imprimir la variable habilidad del diccionario 3\n")#Explicamos lo que hara el codigo brevemente con un print
busqueda = vengador3["Habilidad"] #Pedimos que imprima un dato en especifico de uno de los 3 diccionarios
print(busqueda)#Imprimimos la variable pedida

print("\n -> Imprimimos el primer diccionario completo\n")#Explicamos lo que hara el codigo brevemente con un print
print(vengador1)#Imprimimos eñ primer diccionario completo

# -> TEMA 2: Modificar valores de un diccionario

print("\n -> Modificar la variable nombre del diccionario 1\n")#Explicamos lo que hara el codigo brevemente con un print
vengador1["Nombre"] = "Natasha Romanoff/Black Widow" #Indicamos que se cambie el valos del nombre del diccionario 1
print(vengador1["Nombre"])#Verificamos que se haya cambiado el dato

# -> TEMA 3: Diccionarios con el bucle for

print("\n -> Imprimir las claves diccionario 2\n")#Explicamos lo que hara el codigo brevemente con un print
for x in vengador2: #Le pedimos que nos de las claves del segundo diccionario
    print(x) #Va a ir imprimiendo clave por clave por vuelta al bucle

print("\n -> Imprimir los datos diccionario 3\n")#Explicamos lo que hara el codigo brevemente con un print
for x in vengador3: #Le pedimos que nos de los datos guardados del tercer diccionario
    print(vengador3[x]) #Va a ir imprimiendo dato por dato por vuelta al bucle

# -> TEMA 4: Contar elementos que se encuentren en un diccionario

print("\n -> Imprimir cuantos elementos hay en diccionario 2\n")#Explicamos lo que hara el codigo brevemente con un print
print(len(vengador2))#Nos dira que tantos elementos hay en el diccionario 2

# -> TEMA 5: Eliminar todo o una parte de un diccionario

del vengador3["Estado"] #Indicamos que se elimine el elemento estado
print(vengador3) #Verificamos que se haya eliminado

# -> TEMA 6: Añadir algo a un diccionario

vengador3["Hijos?"] = "Si" #Añadimos un nuevo elemento al diccionario 3
print(vengador3) #Verificamos que se haya agregado
