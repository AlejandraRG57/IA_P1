#Alejandra Rodriguez Guevara 21310127 6E1

# -> TEMA: Clases y Objetos
print("\n -> Creamos una clase y objetos y practicamos su uso \n")#Explicamos lo que hara el codigo brevemente con un print

class Libros:   #Declaramos una nueva clase llamada Libros
    nombre = "" #Ponemos el atributo nombre
    autor = "" #Ponemos el atributo autor
    def repositorio(self):  #creamos una funcion llamada repositorio
        print("Nombre: ", self.nombre, "\nAutor: ", self.autor) #imprimimos la clase con los datos guardados

libro1 = Libros() #Hacemos libro 1 un objeto dentro de la clase libros

libro1.nombre = "Harry Potter" #Asignamos el nombre de un libro al atributo nombre
libro1.autor = "J.K. Rowley" #Asignamos el autor del libro al atributo autor

libro1.repositorio() #Imprimimos los valores de los atributos de la clase

# -> TEMA 2: Metodo __init__
print("\n -> Lo mismo que el anterior pero con __init__ \n")#Explicamos lo que hara el codigo brevemente con un print

class Marvel:   #Declaramos una nueva clase llamada Marvel
    def __init__(self, nombre, clave): #Definimos una funcion __init__ 
        self.nombre = nombre #Ponemos el atributo nombre
        self.clave = clave #Ponemos el atributo clave
    
    def basedatos(self):  #creamos una funcion llamada basedatos
        print("Nombre: ", self.nombre, "\nClave: ", self.clave) #imprimimos la clase con los datos que nos den

aveng1 = Marvel("Natasha","Black Widow") #Hacemos aveng1 un objeto dentro de la clase Marvel y le damos datos
aveng1.basedatos()#Imprimimos los valores de los atributos de la clase


# -> TEMA 3: Cambiar valores establecidos
print("\n -> Amprendemos a modificar datos de la clase anterior \n")#Explicamos lo que hara el codigo brevemente con un print

aveng1.nombre = "Natasha Romanoff" #Modificamos el dato del atributo nombre
aveng1.basedatos() #Imprimimos los valores de los atributos de la clase paara verificar que se modificaran

# -> TEMA 4: Declarar clases vacias
print("\n -> Aprendemos a hacer clases vacias \n")#Explicamos lo que hara el codigo brevemente con un print

class Claseolvidada: #Declaramos la clase
    pass # La dejamos vacia con el pass

# -> TEMA 5: Eliminar atributos de objetos
print("\n -> Aprendemos a eliminar atributos \n")#Explicamos lo que hara el codigo brevemente con un print

del aveng1.nombre #Eliminamos el atributo nombre

# -> TEMA 6: Eliminar objetos
print("\n -> Aprendemos a eliminar objetos \n")#Explicamos lo que hara el codigo brevemente con un print

del aveng1 #Eliminamos el objeto aveng1
