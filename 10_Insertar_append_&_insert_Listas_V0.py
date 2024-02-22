#Alejandra Rodriguez Guevara 21310127 6E1

# -> Insertar elementos con append()
print("\n\t -> Insertar elementos con append()\n")#Le damos un titulo

vengadores = ["append","Iron Man","Black Widow", "Capitan America", "Hulk","Hawkeye"]#Creamos una lista a la que añadiremos un elemento
vengadores.append("Wanda Maximof")#Este  metodo solo añadira el elemento nuevo al final de la lista
print(vengadores)#Verificamos que se haya añadido

#Ejercicio
#Nos pide añadir los colores fuxia y celeste a la lista
print("\n Ejercicio 1 \n")#Le damos un subtitulo

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Escribimos la lista que se nos dio
colores.append("fuxia")#Añadimos el primer color pedido
colores.append("celeste")#Añadimos el segundo color pedido
print(colores)#Verificamos que se hayan añadido


# -> Insertar elementos con insert()
print("\n\t -> Insertar elementos con insert()\n")#Le damos un titulo

marvel = ["insert","Kate Bishop", "Wanda Maximof", "Natasha Romanoff", "Yelena Belova", "Carol Danvers", "Kamala Khan"]#Creamos otra lista para añadirle elementos con el nuevo metodo
marvel.insert(3,"Shuri")#Añadimos un nuevo elemento en la posicion 3
marvel.insert(-2,"Okoye")#Intentamos usar posiciones negativas
print(marvel)#Verificamos que se hayan añadido

#Ejercicio2
#Nos pide añadir los colores magenta y turquesa a la lista en pociiones determinadas
print("\n Ejercicio 2 \n")#Le damos un subtitulo

colores2 = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Escribimos la lista que se nos dio
colores2.insert(6, "magenta")#Insertamos magenta despues de lila
colores2.insert(-1, "turquesa")#Insertamos turquesa en la penultima posicion
print(colores2)#Verificamos que los hayamos añadido correctamente
