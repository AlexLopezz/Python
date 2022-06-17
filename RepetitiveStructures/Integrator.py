'''Construya un algoritmo capaz de encontrar todas las cifras de tres digitos
que cumplan con la condicion de que la suma de los cubos de sus digitos
sea igual al numero que la cifra representa'''

#Forma 1:
for i in range(100,1000):
	unit = i % 10  #Asi sacamos la unidad de un numero...
	ten = (i // 10) % 10 #Asi se saca la decena de un numero...
	hundred = i // 100    #Y asi la centena. La boble barra ( // ) significa division con resultado entero.
	total = (unit**3 + ten**3 + hundred**3)
	if total == i:
		print(i)

#Forma 2: 
for it in range(100,1000):
	strNumber = str(it) #Convertimos a string el numero...
	total2 = 0 #Aqui acumularemos el resultado final
	for x in strNumber: #Recorremos el string generado y..
		total2 += int(x)**3 #Volvemos a convertir a int cada uno de los elementos del string y lo exponemos al cubo
	if total2 == it: #Preguntamos, si el total acumulado es lo mismo que it...
		print(it) #Si es asi, entonces imprimimos por pantalla

