'''DADO EL MONTO DE COMPRA DE UN CLIENTE
si LA COMPRA es MAYOR A #10000 DESCONTAR 5%
si la compra es mayor a 15000 descontar 10%
si la compra es mayor a 50000 descontar un 20%
si la compra es mayor a 100000 descontar un 30%
MOSTRAR AL FINAL EL MONTO TOTAL Y EL DESCUENTO REALIZADO '''

totalPrice = float(input("Ingrese el valor de la compra: "))
discountPrice = 0 #Inicializamos la variable descuento, por ahora en 0.

if totalPrice > 100000:
	discountPrice = totalPrice * 0.3
	totalPrice -= discountPrice
	print(f"Total a pagar: {totalPrice}.->Descuento efectuado de %30. (${discountPrice})")
elif totalPrice > 50000:
	discountPrice = totalPrice * 0.2
	totalPrice -= discountPrice
	print(f"Total a pagar: {totalPrice}.->Descuento efectuado de %20. (${discountPrice})")
elif totalPrice > 15000:
	discountPrice = totalPrice * 0.1
	totalPrice -= discountPrice
	print(f"Total a pagar: {totalPrice}.->Descuento efectuado de %10. (${discountPrice})")
elif totalPrice > 10000: 
	discountPrice = totalPrice * 0.05
	totalPrice -= discountPrice
	print(f"Total a pagar: {totalPrice}.->Descuento efectuado de %5. (${discountPrice})")
else: 
	print(f"Total a pagar: {totalPrice}.->No se aplicaron descuentos.")

