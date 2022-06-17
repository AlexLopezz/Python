'''Se leen tres números que son las longitudes de los lados de un triángulo.
Determinar e informar si el mismo es:
equilátero (3 lados iguales)
isósceles (2 lados iguales)
escaleno (3 lados distintos). '''

long1= int(input("Ingrese la longitud de L1: "))
long2= int(input("Ingrese la longitud de L2: "))
long3= int(input("Ingrese la longitud de L3: "))

if long1 == long2 and long2== long3:
	print("El triangulo es EQUILATERO.")
elif long1== long2 and long2 != long3 or long3==long1 and long1!=long2 or long2== long3 and long2 != long1:
	print("EL triangulo es ISOSCELES.")
else:
	print("El triangulo es ESCALENO.")