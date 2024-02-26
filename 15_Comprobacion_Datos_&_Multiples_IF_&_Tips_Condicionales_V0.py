#Alejandra Rodriguez Guevara 21310127 6E1

# -> TEMA: Buscar datos en listas y tuplas

marvel = ["Kate Bishop", "Wanda Maximof", "Natasha Romanoff", "Yelena Belova", "Kamala Khan"]#Declaramos una lista
print("Natasha Romanoff" in marvel)#Pedimos que imprima un true si si encuentra a "Natasha Romanoff" en la lista
print("Vision" in marvel)#Ahora le pedimos un valor que sabemos que no esta en la lista para que nos regrese un False


#Usando el tema del capitulo anterior usaremos un if-else e input() para que un usuario pregune si cierto dato esta en la lista

pregunta = input("Menciona un artista que crees que sea de los mas escuchados en spotify 2023\n")#Le pedimos a el usuario que nos de el nombre de un artista que crean que se escucha mucho en spotify
cantantes = ["Taylor Swift", "Bad Bunny", "The Weeknd", "Drake","Peso Pluma"]#Declaramos otra lista
if pregunta in cantantes:
    print("Si ese es uno de los top 5 mas escuchados en spotify 2023")#En caso de si estar en la lista se lo mencionamos al usuario
else:
    print("No, ese no llego a la lista,chance el proximo año lo logra")#En caso de no encontrarse en la lista se le dice al usuario que no esta


# -> TEMA: Multiples IF, sin usar else o elif

pregunta = int(input("¿Cual de estos numeros eliges? -> 7 , 5 , 9 , 13 \n"))#Le pedimos al usuario que elija uno de los siguientes numeros 7 , 5 , 9 , 13

if pregunta == 7:
               print("Seh ese numero es el mejor")#Se entrega una respuesta pre guardada depende del numero que nos de
if pregunta == 5:
               print("Ese numero es bueno")#Se entrega una respuesta pre guardada depende del numero que nos de
if pregunta == 9:
               print("Buena respuesta, supongo...")#Se entrega una respuesta pre guardada depende del numero que nos de
if pregunta == 13:
               print("Sin comentarios")#Se entrega una respuesta pre guardada depende del numero que nos de
#En caso de dar alguna valos que no este en las opciones solo se sale del programa

# -> TEMA: Tips para abreviar condicionales

var1 = 7
var2 = 5
if var1>var2: print("Supremacia del 7 sobre el 5")#Nos enseñan que nos podemos ahorrar lineas de codigo poniendo codigos breves en una misma linea

#Nos mencionan que el uso de and y or es bastante util, lo pondremos a prueba
legal = int(input("¿Cual es tu edad?\n"))
cred = input("¿Tienes identificacion? Si/No\n")

if legal <= 17 or cred == "No": print("No puedes entrar")#Probamos poner opciones tanto de strings como de int, y a su vez probamos la condicional or
elif legal >=18 and cred == "Si": print("Pasele camarada")#Aqui tambien mezclamos tipos de variables y hacemos uso del operador and

