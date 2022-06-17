#Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.

print("Consigna 4: Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.")

numberM = int(input("->Ingrese por favor el dividendo: "))
numberN = int(input("->Ingrese por favor el divisor: "))
if (numberM % numberN) == 0:
	print(f"El numero {numberN} es divisor de {numberM}.")
else:
	print(f"El numero {numberN} No es divisor de {numberM}.")
	