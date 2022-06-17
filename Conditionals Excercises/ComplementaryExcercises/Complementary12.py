'''Hacer un programa que imprima el nombre de un artículo, clave, precio original y su precio con descuento.
El descuento lo hace en base a la clave, si la clave es 01 el descuento es del 10% y si la clave es 02 el
descuento en del 20% (solo existen dos claves). '''

nameArticle= input("->Ingrese el nombre del articulo: ")
key= input("->Ingrese la clave: ")
price= float(input("->Ingrese el precio: "))

if key == '01':
	discount = price * 0.10
	discountPrice= price-discount
elif key == '02':
	discount = price * 0.20
	discountPrice= price-discount

print("-------RESULTADOS------")
print(f"Nombre del articulo: {nameArticle}\n->Clave:{key}\n->Precio original: ${price}\n->Precio con descuento: ${discountPrice}")
