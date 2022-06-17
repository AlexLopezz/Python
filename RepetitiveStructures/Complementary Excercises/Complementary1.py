'''  Determinar el número mayor de 10 números ingresados. '''

biggerNumber=0 #Con esta variable guardaremos el numero mayor.

for it in range(0,10):
	number=int(input("->Ingrese por favor un numero: "))
	if number > biggerNumber: #En la primera iteracion, siempre entrara en el if, pero luego, empezara a comparar...
		biggerNumber= number

print(f"->El numero mayor es: {biggerNumber}")
