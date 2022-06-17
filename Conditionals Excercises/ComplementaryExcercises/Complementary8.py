'''Calcular el número de pulsaciones que una persona debe tener
por cada 10 segundos de ejercicio, si la fórmula es: Número de pulsaciones = (220 - edad)/10'''

print("Para saber el numero de pulsaciones que debe tener, nos debe ingresar su edad.")
age = int(input("->Ingrese por favor su edad: "))
if age > 0:
	pulsesNumber= (220 - age)/10
	print(f"El numero de pulsaciones que usted debe tener por cada 10 segundos de ejercicios es: {pulsesNumber}")
else:
	print(f"No existe una persona que tenga {age} años...")