'''Diseñar un programa que lea las longitudes de los
tres lados de un triángulo (L1,L2,L3) y determine qué
tipo de triángulo es, de acuerdo a los siguientes casos.

*Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:

Si A>=B + C à No se trata de un triángulo

Si A2 = B2 + C2 à Es un triángulo rectángulo

Si A2 > B2 + C2 à Es un triángulo obtusángulo

Si A2 < B2 + C2 à Es un triángulo acutángulo '''

A= int(input("Ingrese la longitud de L1: "))
B= int(input("Ingrese la longitud de L2: "))
C= int(input("Ingrese la longitud de L3: "))

if A > B and A > C:
	if A >= (B+C):
		print("No es un triangulo.")
	elif A**2 == (B**2+C**2):
		print("Es un triangulo rectangulo.")
	elif A**2 > (B**2 + C**2):
		print("Es un triangulo obtusangulo.")
	elif A**2 < (B**2+C**2):
		print("Es un triangulo acutangulo.")

