'''En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número
que se escoge al azar. Si el numero escogido es menor que 74 el descuento es del 15% sobre el total de la compra
 si es mayor o igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta. '''

totalPrice= float(input("Ingrese por favor el precio total de la compra: $"))
numberClient= int(input("Ingrese un numero al azar: "))
if numberClient < 74:
	discountPrice= totalPrice*0.15
	print(f"->El descuento es del 15%.\nEl dinero que se le descuenta es de: ${discountPrice}")
else:
	discountPrice= totalPrice*0.20
	print(f"->El descuento es del 20%.\nEl dinero que se le descuenta es de: ${discountPrice}")



