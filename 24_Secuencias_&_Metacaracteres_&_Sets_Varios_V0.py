#Alejandra Rodriguez Guevara 21310127 6E1

# -> TEMA: Metacaracteres
print("\n -> Metacaracteres \n")#Explicamos lo que hara el codigo brevemente con un print

import re # Importamos el módulo re

texto = "Somebody once toold me 5 7 the $ world is gonna roll me"# Definimos un string sobre el que vamos a realizar las búsquedas

find = re.findall("[l-r]", texto)#Le decimos que imprima todas las letras de la l a la r en una lista
find2 = re.findall("to{2}ld", texto)#Le decimos que imprima coincidencias en el texto en una lista 
find3 = re.findall("world|planet", texto)#Le decimos que imprima world o planet en el texto en una lista
find4 = re.findall("Som...dy", texto)#Le decimos que imprima una letra que tenga las coincidencias Som...dy en una lista
find5 = re.findall("^Some", texto)#Le decimos que imprima una palabra que inicie con some en una lista en una lista

print(find)#  Imprimimos la lista de coincidencias encontradas
print(find2)# Imprimimos la lista de coincidencias encontradas
print(find3)# Imprimimos la lista de coincidencias encontradas
print(find4)# Imprimimos la lista de coincidencias encontradas
print(find5)# Imprimimos la lista de coincidencias encontradas

# -> TEMA2: Secuencias especiales
print("\n -> Secuencias especiales \n")#Explicamos lo que hara el codigo brevemente con un print

find6 = re.findall("\ASomebody", texto)#Le decimos que imprima coincidencias donde los caracteres especificados estan al inicio de la cadena en una lista
find7 = re.findall("rl\B", texto)#Le decimos que imprima coincidencias donde los caracteres especificados estan en medio de una palabra, pero no al inicio ni final, en una lista

print(find6)#  Imprimimos la lista de coincidencias encontradas
print(find7)# Imprimimos la lista de coincidencias encontradas


# -> TEMA3: Sets
print("\n -> Sets \n")#Explicamos lo que hara el codigo brevemente con un print

find8 = re.findall("$", texto)#Le decimos que imprima coincidencias donde $ este presente en  una lista
find9 = re.findall("o", texto)#Le decimos que imprima coincidencias donde los caracteres especificados esten en la lista
find10 = re.findall("[l-r]", texto)#Le decimos que imprima todas las letras en cierto rango
find11 = re.findall("^z", texto)#Le decimos que imprima coincidencias donde los caracteres especificados no esten en la lista
find12 = re.findall("[5-7]", texto)#Le decimos que imprima todos los numeros en cierto rango
find13 = re.findall("[l-rL-R]", texto)#Le decimos que imprima todas las letras en cierto rango sin importar si es mayuscula o minuscula

print(find8)#  Imprimimos la lista de coincidencias encontradas
print(find9)# Imprimimos la lista de coincidencias encontradas
print(find10)# Imprimimos la lista de coincidencias encontradas
print(find11)# Imprimimos la lista de coincidencias encontradas
print(find12)# Imprimimos la lista de coincidencias encontradas
print(find13)# Imprimimos la lista de coincidencias encontradas
