#Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.

greaterNumber=0
leastNumber=0
print("La consigna del ejercicio me pide que a continuacion que me digite 3 numeros...")

number1 = int(input("Ingrese por favor el primer numero: "))
number2 = int(input("Ingrese por favor el segundo numero: "))
number3 = int(input("Ingrese por favor el tercer y ultimo numero: "))

#Decifrar mayor...
if number1>number2 and number1>number3:
	greaterNumber= number1
elif number2 > number1 and number2 > number3:
	greaterNumber= number2
else:
	greaterNumber= number3

#Decifrar menor...
if number1< number2 and number1< number3:
	leastNumber= number1
elif number2 < number1 and number2 < number3:
	leastNumber= number2
else:
	leastNumber= number3

print("->El numero menor es: ", leastNumber)
print("->El numero mayor es: ", greaterNumber)
