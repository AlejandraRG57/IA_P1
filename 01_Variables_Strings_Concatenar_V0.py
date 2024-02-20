#Alejandra Rodriguez Guevara 21310127 6E1
#Uso de Variables, Strings y Concatenar Strings

#------>Variables

variables = "Aqui practicamos variables"#Usamos un string
print(variables)#Lo imprimimos
b=3 #Declaramos la variable "b"
c=4 #Declaramos la variable "c"
d=b+c #Planteamos la suma de las dos variables "b y c" y lo almacenamos en la variable "d"
print(d) #Imprimimos el resultado de la suma planteada

#------>Strings

string = "-Hola mundo-" #A la variable "string" le almacenamos el string hola mundo
print(string) #Imprimimos el string
string2 = '-Hola mundo-' #Tambien se pueden usar las comillas simples para los strings
print(string2) #Imprimimos el string
string3 = '"print()" se utiliza para imprimir valores en la consola.' #Los dos tipos de comillas sirven para poder usar las comillas dentro de un string
print(string3) #Imprimimos el string
string4 = "-Hello world es 'hola mundo' en ingles-" #Tambien funciona al reves
print(string4) #Imprimimos el string

#------>Concatenar

#-Concatenar strings

Intro = "Hola" + " Mundo"  #Concatenamos dos strings en una misma variable
print(Intro)#Imprimimos la variable

palabra1 = "Hello " #Primer string
palabra2 = "World" #Segundo string
Intro = palabra1 + palabra2 #Concatenamos los strings de dos variables en una tercera variable
print(Intro)

word = "Todos" #Declaramos la variable
print(word + "mienten") #Aqui concatenamos el valor string de una variable con un valor string

palabra1 = "Alejandra" #Nombre
palabra2 = "Rodriguez" #Primer apellido
palabra3 = "Guevara" #Segundo apellido
nombre_completo = palabra1 + ' ' + palabra2 + ' ' + palabra3 #Se unen los tres strings y se le añaden espacios con comillas
print(nombre_completo) #Imprimimos el string resultante

#-Concatenar numeros

#declaramos dos variables
num1 = 5 #variable 1
num2 = 7 #variable 2
suma1= num1 + num2 #Lo intentamos concatenar como con el string
print(suma1) #No se concatenan, se suman por ende se haria como abajo

num1 = "5" #variable 1 con comillas
num2 = "7" #variable 2 con comillas
suma1= num1 + num2 #Procedemos a concatenar
print(suma1)#Se concatenan correctamente
