''' 2) Desarrollar una solución que calcule la suma de los cuadrados
de los n primeros números naturales: 1 + 22 + 32 +… + n2. '''

print("Programa que calcula la suma de los cuadrados")
amountNumberNaturals = int(input("Ingrese por favor la cantidad de numeros naturales que desea calcular: "))

square=0
plusNUmber = 0
for it in range(1,amountNumberNaturals):
	square= it*it
	plusNUmber+= square
	print(f"*El cuadrado del numero {it} es {square}")
print(f"-> La suma de los cuadrados de los {amountNumberNaturals} primeros numeros naturales, es de : {plusNUmber}")
