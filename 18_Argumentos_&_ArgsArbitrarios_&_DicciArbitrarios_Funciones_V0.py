#Alejandra Rodriguez Guevara 21310127 6E1 

# -> TEMA: Funciones

print("\n -> Creamos una nueva funcion con una variable guardada\n")#Explicamos lo que hara el codigo brevemente con un print
def refran(): #Creamos una nueva funcion
    print("Pez que se duerme se lo lleva la corriente") #Guardamos lo que queremos que se imprima
refran() #Verificamos si si se creo la funcion y si se guardaron los datos

# -> TEMA 2: Argumentos en Funciones

print("\n -> Creamos dos nuevas funciones con variables guardadas y usamos argumentos\n")#Explicamos lo que hara el codigo brevemente con un print
def Jarvis(nombre, clave): #Creamos una nueva funcion con argumentos
    print("Bienvenido", nombre, clave) #Guardamos lo que queremos que se imprima y le ponemos argumentos
Jarvis("Natasha", "Black Widow") #Verificamos si si se creo la funcion y le guardamos datos en los argumentos
Jarvis("Tony", "Iron Man") #Verificamos otra vez si si se creo la funcion y le guardamos datos en los argumentos

# -> TEMA 3: *args en funciones

print("\n -> Creamos una nueva funcion y usamos args para rellenar los datos pedidos\n")#Explicamos lo que hara el codigo brevemente con un print
def disney(*args): #Creamos una nueva funcion con *args
    print("Primer personaje " + args[0] + " ultimo personaje "+ args[3] ) #Guardamos lo que se imprimira y le especificamos que args usar
disney("Nemo","Dory","Tiger","Mickey") #Mandamos a llamar a la funcion y le agregamos args

# -> TEMA 4: **kwargs en funciones

print("\n -> Creamos una nueva funcion y usamos kwargs para rellenar los datos pedidos\n")#Explicamos lo que hara el codigo brevemente con un print
def pizzas (**kwargs): #creamos una funcion con **kwargs
	print("Este es un tipo de pizza: " + kwargs['pizza1'] )#Guardamos lo que se imprimira y le especificamos que kwargs tomar
pizzas(pizza1='Margarita', pizza2='Pizza de sarten')#Mandamos a llamar a la funcion y le agregamos kwargs
