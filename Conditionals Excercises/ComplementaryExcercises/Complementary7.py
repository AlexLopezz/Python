'''Un comercio ofrece un descuento del 15% sobre el total de la
compra si esta supera los $1000. Obtenga para determinado cliente
cuánto deberá pagar finalmente por su compra y el descuento
obtenido, si es que corresponde.'''

totalPrice = float(input("Ingrese por favor el total de la compra: $"))
if totalPrice > 1000:
	discountPrice= totalPrice * 0.15
	totalPrice-= discountPrice
	print(f"->El precio total a pagar es de: ${totalPrice}.")
	print(f"->Se aplico un descuento del 15% de descuento (${discountPrice}) debido a que su compra supero los $1000")
else: 
	print(f"->El precio total a pagar es de: ${totalPrice}")
