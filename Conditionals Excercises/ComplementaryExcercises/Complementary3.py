#Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.

print("Consigna 3: Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.")
setOfNumbers = input("->Ingrese por favor un conjunto de tres numeros: ")
if len(setOfNumbers) == 3:
	number1 = int(setOfNumbers[0])
	number2 = int(setOfNumbers[1])
	number3 = int(setOfNumbers[2])
	if number1 < number2 and number1 < number3: 
		print(f"El numero {number1} ES MENOR que {number2} y {number3}")
	else:
		print(f"El numero {number1} NO ES MENOR que {number2} y {number3}")
else:
	print("[X]Error, usted no obedecio a la consigna.")
