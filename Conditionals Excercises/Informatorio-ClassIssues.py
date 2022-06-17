'''DADO EL MONTO DE COMPRA DE UN CLIENTE, OFRECER UN DESCUENTO DEL 10%. 
SIEMPRE Y CUANDO LA COMPRA SEA MAYOR A #10000
PERO SI LA MISMA ES MENOR O IGUAL A 10000 INCREMENTARLE UN 5% '''

totalPrice = float(input("Ingrese el valor de la compra: "))
discountPrice = 0 #Inicializamos la variable descuento, por ahora en 0.

if totalPrice <= 1000: #Analizamos la primer condicion...
	discountPrice = (totalPrice * 0.05) #Descuento del 5% 
	totalPrice += discountPrice 
else: #Tambien podria ir elif .... Pero opte por un else.
	discountPrice = totalPrice * 0.1 #Descuento del 10%
	totalPrice -= discountPrice

print(f"El monto a pagar en total es de: {totalPrice}") #Mostramos por pantalla el precio a pagar.