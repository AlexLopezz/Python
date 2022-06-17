'''Diseñar un programa que permita calcular el total de una compra, ingresando cantidad
y precio de los productos. El programa debe estar preparado para que el ingreso de los
datos se produzca hasta que el usuario lo desee '''

follow= True
price = 0
totalPrice = 0
while(follow):
	price = float(input("-> Ingrese el precio unitario del producto: "))
	amount = int(input("-> Ingrese la cantidad del producto: "))
	totalPrice+= price * amount 
	print(f"El total a pagar es: ${totalPrice}")

	strDecision= input("Desea volver a cargar datos? Presione 's', de lo contrario cualquier tecla...\nRespuesta: ")
	if strDecision.lower() != 's':
		follow = False



