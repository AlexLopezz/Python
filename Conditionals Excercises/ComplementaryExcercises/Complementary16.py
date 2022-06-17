'''Hacer un programa que calcule el total a pagar por la compra de camisas. Si se compran tres camisas o mas
se aplica un descuento del 20% sobre el total de la compra y si son menos de tres camisas un descuento del 10%. '''

amountT_shirts= int(input("Ingrese la cantidad de camisas compradadas: "))
if amountT_shirts > 0:
	price = float(input("Ingrese el precio total a pagar por la compra de camisas: $"))
	if amountT_shirts>= 3:
		discountPrice= price * 0.20
		print(f"El precio total a pagar es de: ${price-discountPrice}.\nMotivo del descuento: Compra de 3 o mas camisas. Dto del %20")
	else:
		discountPrice= price * 0.10
		print(f"El precio total a pagar es de: ${price-discountPrice}.\nMotivo del descuento: Compra menor a 3 camisas. Dto del %10")


else:
	print("No podra saber si obtiene descuentos por la compra de camisas, debido a que debe digitar un numero mayor a cero.")