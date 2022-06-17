''' Un local vende remeras por mayor y menor
Si la compra es por una cantidad mayor o igual a 10 remeras
el precio por unidad es de tan solo el 80%.

Preguntar cuantas unidades de remeras se incluyen en la compra
y el precio por unidad.
Devovlver el precio total de la compra. '''


PriceUnit = float(input("Ingrese el precio unitario de la remera: "))
NumberOfT_Shirts = int(input("Ingrese por favor la cantidad de remeras: "))
TotalPrice = 0
if NumberOfT_Shirts >= 10:
	TotalPrice = (PriceUnit * NumberOfT_Shirts) * 0.8
else:
	TotalPrice = PriceUnit * NumberOfT_Shirts 

print(f"El precio total de la compra es de: {TotalPrice}") 