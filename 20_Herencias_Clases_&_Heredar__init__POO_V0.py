#Alejandra Rodriguez Guevara 21310127 6E1

# -> TEMA: Herencia de clases
print("\n -> Creamos una clase y objetos y practicamos la creacion y uso de herencias \n")#Explicamos lo que hara el codigo brevemente con un print

class BasicMemb: #Declaramos nuestra clase
    def __init__(self, nombre, apellido1, apellido2): #Definimos una funcion __init__ 
        self.nombre = nombre #Creamos el atributo nombre
        self.apellido1 = apellido1 #Creamos el atributo apellido1
        self.apellido2 = apellido2 #Creamos el atributo apellido2
        
    def printdatos(self): #Creamos una funcion llamada printdatos
        print("Nombre:", self.nombre,"\nApellido1:",self.apellido1,"\nApellido2:",self.apellido2)#imprimimos la clase con los datos que nos den

random = BasicMemb("Tobias","Harrik","Menendes")#Hacemos random un objeto dentro de la clase BasicMemb y le damos datos
random.printdatos()#Imprimimos los valores de los atributos de la clase

class PremiumMemb(BasicMemb): #Declaramos noestra subclase y llamamos los atributos y metodos de la superclase a esta
    def __init__(self, nombre, deporte, pago):
        self.nombre = nombre #Creamos el atributo nombre
        self.deporte = deporte #Creamos el atributo deporte
        self.pago = pago #Creamos el atributo pago
    def printdatos2(self): #Creamos una funcion llamada printdatos2
        print("Nombre:", self.nombre,"\nDeporte:",self.deporte,"\nHa pagado?:",self.pago)#imprimimos la clase con los datos que nos den


# -> TEMA2: Heredar el metodo __init__
print("\n -> Creamos una subclase y objetos y practicamos su uso \n")#Explicamos lo que hara el codigo brevemente con un print

#Como arriba hicimos, si en nuestra subclase ponemos otro metodo __init__ se utilizara para la subclase el suyo, ya que este predomina

fancy = PremiumMemb("Thomas","Tenis","Si")#Hacemos fancy un objeto dentro de la subclase PremiumMemb y le damos datos
fancy.printdatos2()#Imprimimos los valores de los atributos de la subclase
