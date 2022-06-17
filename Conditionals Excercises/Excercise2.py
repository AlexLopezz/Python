''' Ingresar la edad de una persona por teclado
Mostrar mensaje indicando si es mayor o menor de dad '''

age = int(input("Ingrese por favor su edad: "))
isOlder = False
if age >= 18:
	isOlder = True

if isOlder == True:
	print("Usted es mayor de edad")
elif isOlder == False:
	print("Usted es menor de edad")


