'''Leer 2 números;si son iguales que los multiplique
 si el primero es mayor que el segundo que los reste y si no que los sume. '''

number= int(input("Ingrese el primer numero: "))
number2= int(input("Ingrese el segundo numero: "))

if number == number2:
 	print(f"->Son iguales: {number} x {number2} = {number*number2}")
elif number > number2:
 	print(f"->El primer numero es mayor al segundo: {number} - {number2} = {number-number2}")
else:
	print(f"->El segundo numero es mayor que el primero: {number} + {number2} = {number+number2}")