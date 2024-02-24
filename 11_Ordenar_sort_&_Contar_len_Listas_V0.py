#Alejandra Rodriguez Guevara 21310127 6E1

# -> Ordenar elementos con sort() y sorted()
print("\n\t -> Ordenar elementos con sort() y sorted()\n")#Le damos un titulo

cantantes = ["Camila Cabello", "Katy Perry", "Eminem", "Morat", "Paulo Londra"]#Creamos una lista
cantantes.sort()#Utilizamos el metodo sort
print(cantantes)#Verificamos que se hayan ordenado

cantantes.sort(reverse=True)#Utilizamos el metodo sort pero inverso
print(cantantes)#Verificamos que se hayan invertido
print(cantantes[1])#Imprimimos el elemento que este en la posicion 1, el cual es morat al haber sido ordenado inversamente

vengadores = ["Iron Man","Black Widow", "Capitan America", "Hulk","Hawkeye"]#Creamos otra lista
print(sorted(vengadores))#Utilizamos el metodo sorted para que sea temporal su ordenamiento
print(vengadores)#Verificamos que no esten ordenados

#Ejercicio 1
#Nos piden ordenar esta lista que nos dieron en orden alfabetico inverso
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Escribimos la lista que nos dan
colores.sort(reverse=True)#Utilizamos el metodo sort pero inverso
print(colores)#Verificamos que este correcto


# -> Contar elementos con len()
print("\n\t -> Contar elementos con len()\n")#Le damos un titulo

marvel = ["Kate Bishop", "Wanda Maximof", "Natasha Romanoff", "Yelena Belova", "Carol Danvers", "Kamala Khan"]#Creamos otra lista
print(len(marvel))#Utilizamos el metodo len para contar los elementos y lo imprimimos
cantidad = len(marvel) #Almacenamos cuantos personajes hay en una variable
print("Son",cantidad,"increibles vengadores que conforman nuestra lista")#Probamos usar el dato que guardamos en una variable
