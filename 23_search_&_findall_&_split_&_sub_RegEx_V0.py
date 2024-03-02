#Alejandra Rodriguez Guevara 21310127 6E1

# -> TEMA: Expresion regular search()
print("\n -> Utilizamos la funcion search \n")#Explicamos lo que hara el codigo brevemente con un print

import re #Importamos el modulo re

frase = "Somebody Once told me..." #Escribimos una frase random
find = re.search("o", frase)#Le decimos que busque la letra o en la frase, cuando la encuentre se imprimira la palabra match
nofind = re.search("p", frase)#Le decimos que busque la letra p en la frase, en caso de no encontrarla nos regresara un None
palabra = re.search("Somebody", frase)#Le decimos que busque la palabra "Somebody" en la frase, cuando la encuentre se imprimira la palabra match
print(find)#Imprimimos si se encontro o no la letra
print(nofind)#Imprimimos si se encontro o no la letra
print(palabra)#Imprimimos si se encontro o no la palabra

# -> TEMA2: Expresion regular findall()
print("\n -> Utilizamos la funcion findall \n")#Explicamos lo que hara el codigo brevemente con un print

frase = "Somebody Once told me..." #Escribimos una frase random
find = re.findall("o", frase)#Le decimos que busque la letra o en la frase, cuando las encuentre se imprimiran todas la o que hay en la frase en una lista
nofind = re.findall("p", frase)#Le decimos que busque la letra p en la frase, en caso de no encontrarla nos regresara una lista vacia
palabra = re.findall("Somebody", frase)#Le decimos que busque la palabra "Somebody" en la frase, cuando la encuentre se imprimira la palabra la cantidad de veces que salga en una lista
print(find)#Imprimimos lo que encontro
print(nofind)#Imprimimos lo que encontro
print(palabra)#Imprimimos lo que encontro

# -> TEMA3: Expresion regular split()
print("\n -> Utilizamos la funcion split \n")#Explicamos lo que hara el codigo brevemente con un print

frase = "Somebody Once told me..." #Escribimos una frase random
separ = re.split(" ", frase)#Le decimos que separe todas las palabras de la frase
separ2 = re.split("o", frase)#Le decimos que excluya todas las o de la frase
palabra = re.split("Somebody", frase)#Le decimos que excluya la palabra "Somebody" de la frase
print(separ)#Imprimimos lo que separo
print(separ2)#Imprimimos lo que separo
print(palabra)#Imprimimos lo que separo

# -> TEMA4: Expresion regular maxsplit()
print("\n -> Utilizamos la funcion maxsplit \n")#Explicamos lo que hara el codigo brevemente con un print

frase = "Somebody Once told me..." #Escribimos una frase random
separ = re.split(" ", frase, 2)#Le decimos que separe 2 veces la frase
separ2 = re.split("o", frase, 2)#Le decimos que excluya 2 de las o de la frase
print(separ)#Imprimimos lo que separo
print(separ2)#Imprimimos lo que separo

# -> TEMA5: Expresion regular sub()
print("\n -> Utilizamos la funcion sub \n")#Explicamos lo que hara el codigo brevemente con un print

frase = "Somebody Once told me the world is gonna roll me..." #Escribimos una frase random
reem = re.sub(" ", "-" , frase)#Le decimos que todos los espacios los rempace con un -
reem2 = re.sub("me", "you", frase)#Le decimos que remplace los me con you
print(reem)#Imprimimos lo que reemplazo
print(reem2)#Imprimimos lo que reemplazo

# -> TEMA5: Expresion regular sub() con count
print("\n -> Utilizamos la funcion sub limitando el numero de resultados \n")#Explicamos lo que hara el codigo brevemente con un print

frase = "Somebody Once told me the world is gonna roll me..." #Escribimos una frase random
reem = re.sub(" ", "-" , frase, 7)#Le decimos que todos los espacios los rempace con un - pero limitamos el numero de resultados
reem2 = re.sub("me", "you", frase, 1)#Le decimos que remplace los me con you limitamos el numero de resultados
print(reem)#Imprimimos lo que reemplazo
print(reem2)#Imprimimos lo que reemplazo
