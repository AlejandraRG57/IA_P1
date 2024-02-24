#Alejandra Rodriguez Guevara 21310127 6E1

# -> Crear y Manejar tuplas

#Las tuplas sonparecidas a las listas pero estas no se pueden modificar

listas = ["Esto","Es","Una","Lista"]#Ponemos un ejemplo de lista para diferenciarla de una tupla
tuplas = ("Esto","Es","Una","Tupla")#Ponemos un ejemplo de tupla para diferenciarla de una lista
print(listas)#Imprimimos la lista
print(tuplas)#Imprimimos la tupla
print(tuplas[3])#Imprimimos un elemento en especifico de la tupla
tuplas2=(5,7,50,70,"Estos numeros son geniales:")#Hacemos una nueva tupla mezclando numeros y caracteres
print(tuplas2[4],tuplas2[0]+tuplas2[3],"y",tuplas2[1]+tuplas2[2])#Lo imprimimos usando tanto texto como suma de variables y verificamos que este correcto

# -> Convertir tuplas a listas y listas a tuplas

cantantesl = ["Camila Cabello", "Katy Perry", "Eminem", "Morat"]#Primero planteamos una lista
cantantest = tuple(cantantesl)#convertimos nuestra lista a una tupla
print(cantantest)#Verificamos que lo hayamos hecho correctamente
print(type(cantantest))#Verificamos que ahora nuestra lista sea una tupla viendo que tipo de dato es

marvell = ("Kate Bishop", "Wanda Maximof", "Natasha Romanoff", "Yelena Belova")#Ahora planteamos una tupla primero
marvelt = list(marvell)#convertimos nuestra tupla a una lista
print(marvelt)#Verificamos que lo hayamos hecho correctamente
print(type(marvelt))#Verificamos que ahora nuestra tupla sea una lista viendo que tipo de dato es



