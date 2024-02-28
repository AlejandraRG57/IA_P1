#Alejandra Rodriguez Guevara 21310127 6E1

# -> TEMA: Bucle While
print("\n -> TEMA: Bucle While\n")#Ponemos titulo del tema a tratar con un print

x = 5 #declaramos la variable x con valor de 5
y = 70 #declaramos la variable y con valor de 70

print("\nContara de 1 en 1 desde el 5 hasta el 7\n")#Explicamos lo que hara el codigo brevemente con un print
while x <= 7: #Utilizamos una comparativa mientras x sea menor o igual que 7 se seguiran incrementando de 1 en 1 y al llegar a 7 se detiene
    print(x) #Se imprime el valor que tenga x despues de cada bucle
    x+=1 #Se va aumentando de 1 en 1 el valor de x
    
print("\nDisminuira el 70 de 5 en 5 hasta el 50\n")#Explicamos lo que hara el codigo brevemente con un print
while y >= 50: #Mientras y sea mayor que 50 ira disminuyendo el valor de 5 en 5 hasta ser menor que 50
    print(y) #Se imprime el valor que tenga y despues de cada bucle
    y-=5 #Se va disminuyendo de 5 en 5 el valor de y


# -> TEMA 2: Bucle While con break y continue
print("\n -> TEMA 2: Bucle While con break y continue\n")#Ponemos titulo del tema a tratar con un print

print("\nIra aumentando el valor de 10 en 10 desde el 10 hasta ser igual que 70\n")#Explicamos lo que hara el codigo brevemente con un print
z = 10 #declaramos la variable z con valor de 10
while z < 100: #Mientras z sea menor que 100 ira aumentando el valor de 10 en 10 hasta ser igual que 70
    print(z) #Se imprime el valor que tenga z despues de cada bucle
    if z == 70: #ponemos una condicion que si z es igual a 70 se detenga
        break #Break es la variable que detiene el programa
    z += 10 #Se va aumentando de 10 en 10 el valor de z

print("\nIra aumentando el valor de 1 en 1 desde el 1 hasta ser menor que , se saltara e l7 y 15\n")#Explicamos lo que hara el codigo brevemente con un print
a = 1 #declaramos la variable a con valor de 1
while a < 17: #Mientras a sea menor que 17 ira aumentando el valor de 1 en 1 hasta ser menor que 17
    a+=1 #Se va aumentando de 1 en 1 el valor de a
    if a==7 or a==15: #Le ponemos una condicional al valor 7 y 15 que se los salte y no los imprima
        continue #continue es la variable que omite numeros en base a especificaciones
    print(a)#Se imprime el valor que tenga a despues de cada bucle

# -> TEMA 3: Bucle For
print("\n -> TEMA 3: Bucle For\n")#Ponemos titulo del tema a tratar con un print

print("\nImprimira el nombre pedido letra por letra\n")#Explicamos lo que hara el codigo brevemente con un print
for x in "Natasha Romanoff": #Creamos un for en el que cada vuelta del bucle nos almacena una letra de la palabra que le dimos y la va imprimiendo una por una
    print(x)#Este print es lo que va imprimiendo cada variable almacenada

print("\nImprimira la lista pedida palabra por palabra\n")#Explicamos lo que hara el codigo brevemente con un print
marvel = ["Iron Man","Black Widow", "Capitan America", "Hulk","Hawkeye"]#Creamos una lista para probar bucler for con listas
for x in marvel: #Le indicamos que por componente en la lista los vaya imprimiendo por vuelta al bucle
    print(x)#Este print es lo que va imprimiendo cada variable almacenada

# -> TEMA 4: Funcion range()
print("\n -> TEMA 4: Funcion range()\n")#Ponemos titulo del tema a tratar con un print

print("\nImprimira del 0 al 7\n")#Explicamos lo que hara el codigo brevemente con un print
for x in range(8):#Probamos la variable range sin darle una variable de inicio por lo que empezara de 0 hasta donde le pedimos
    print(x)#Imprimimos numero por numero por cada vuelta del bucle

print("\nImprimira del 5 al 7\n")#Explicamos lo que hara el codigo brevemente con un print
for y  in range(5,8):#Probamos la variable range dandole una variable de inicio y de final por ende contara de 5 a 7
    print(y)#Imprimimos numero por numero por cada vuelta del bucle

print("\nImprimira del 55 al 70\n")#Explicamos lo que hara el codigo brevemente con un print
for z  in range(55,75,+5):#Probamos la variable range dandole una variable de inicio, de final y de desplazamiento por ende contara del 55 a 75 de 5 en 5
    print(z)#Imprimimos numero por numero por cada vuelta del bucle
    
