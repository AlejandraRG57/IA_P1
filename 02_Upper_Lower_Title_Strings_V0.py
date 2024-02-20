#Alejandra Rodriguez Guevara 21310127 6E1
#Los metodos upper(), lower() y title()

#Metodo title() -> Hace que la primera letra de cada palabra del string este en mayuscula

titulo = "feliz navidad con title" #Le damos un string a la variable titulo
titulo = titulo.title() #A la variable titulo le decimos que es ella misma pero asignandole un .title() despues
print(titulo) #Imprimimos la variable titulo

#Metodo title() de forma mas breve

titulo = "feliz navidad con title mas breve".title() #Aqui asignamos el string a la variable titulo y a su vez le damos formato con .title()
print(titulo) #Imprimimos la variable titulo

#Metodo upper() -> Hace que todas las letras de cada palabra del string esten en mayusculas

titulo = "feliz navidad con upper".upper() #Aqui asignamos el string a la variable titulo y a su vez le damos formato con .upper()
print(titulo) #Imprimimos la variable titulo

#Metodo lower() -> Hace que todas las letras de cada palabra del string esten en minusculas

titulo = "FELIZ NAVIDAD CON LOWER".lower() #Aqui asignamos el string a la variable titulo y a su vez le damos formato con .lower()
print(titulo) #Imprimimos la variable titulo

#Ejercicios

#1
Nombredelcurso = "enrique barros fernández".title() #Usamos el nombre que se nos dio y le ponermos la primera letra en mayusculas
print(Nombredelcurso) #Imprimimos para verificar que este correcto

#2
Frasedelcurso = "Esta Es Una Frase Para Ser Formateada.".lower() #Usamos la frase que se nos dio y la ponemos completamente en minusculas
print(Frasedelcurso) #Imprimimos para verificar que este correcto

#3
Frasedelcurso2 = "Esta Es Una Frase Para Ser Formateada.".upper() #Usamos la frase que se nos dio y la ponemos completamente en mayusculas
print(Frasedelcurso2) #Imprimimos para verificar que este correcto
