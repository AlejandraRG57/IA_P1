#Alejandra Rodriguez Guevara 21310127 6E1

# -> Eliminar con del

marvel = ["del","Kate Bishop", "Wanda Maximof", "Natasha Romanoff", "Yelena Belova", "Carol Danvers", "Kamala Khan"]#Plantemos la lista
del marvel[3] #Borramos el elemento en la posicion 3
del marvel[5]#Probamos borrando otro elemento
del marvel[-2]#Probamos borrando con posiciones negativas
print(marvel)#Corroboramos que la liste este correcta

#Ejercicio
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Nos piden eliminar los colores azul, marron, negro y rosa de la lista que nos dieron
del colores[0] #Eliminamos el color rojo
del colores[3] #Eliminamos el color marron
del colores[-4] #Eliminamos el color negro
del colores[-3] #Eliminamos el color rosa
print(colores)#Corroboramos que la liste este correcta

# -> Eliminar con remove()

marvel2 = ["remove","Kate Bishop", "Wanda Maximof", "Natasha Romanoff", "Yelena Belova", "Carol Danvers", "Kamala Khan"]#Planteamos la misma lista pero ahora utilizamos otro metodo para borrar
marvel2.remove("Natasha Romanoff") #Eliminamos el elemento especifico Natasha Romanoff
print(marvel2)#Corroboramos que la liste este correcta

#Ejercicio 2
colores2 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Nos pide eliminar los elementos amarillos y rojo de la lista que nos dieron
colores2.remove("amarillo")#Eliminamos el color amarillo
colores2.remove("rojo")#Eliminamos el color rojo
print(colores2)#Corroboramos que la liste este correcta

# -> Eliminar con pop()

cantantes = ["Camila Cabello", "Katy Perry", "Eminem", "Morat", "Paulo Londra"]#Probamos eliminar el ultimo elemento de la lista con pop
cantantes.pop() #Utilizamos el metodo pop}
print(cantantes) #Verificamos que si lo haya eliminado

#Ahora eliminamos otro elemento pero este lo almacenamos

mejorcant = cantantes.pop(0)#Eliminamos el elemento en la posicion 0 y lo almacenamos en la variables mejorcant
print("La mejor cantante es:",  mejorcant)#Imprimimos la variable almacenada

#Ejercicio 3
colores3 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Nos pide eliminar azul y blanco y agregarlos a una nueva lista desde la lista que nos dieron
dalton = colores3.pop(1)#Eliminamos el color azul y lo almacenamos en la variable dalton
dalton2 = colores3.pop(-2)#Eliminamos el color blanco y lo almacenamos en la variable dalton2
print(colores3) #Verificamos que si se hayan eliminado
daltonicos = [dalton , dalton2] #hacemos una nueva lista con los valores
print(daltonicos) #Verificamos la nueva lista

 
