''' Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas. '''

#Logica: En vez de realizar 2*3 = 6, se podria hacer 2+2+2 donde te daria el mismo resultado...

multiplying = int(input("Ingrese el multiplicando: "))
multiplier = int(input("Ingrese el multiplicador: "))
product= 0

for it in range(0,multiplier):
	product+=multiplying

print(f"El resultado es: {product}")