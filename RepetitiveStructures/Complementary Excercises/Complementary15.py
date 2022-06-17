''' En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento
dependiendo de un número que se escoge al azar.
Si el número escogido es menor que 50 el descuento es del 15% sobre el total de la compra
si es mayor o igual a 50 el descuento es del 20%. Obtener cuánto dinero se le descuenta.'''

follow= 'SI'
while follow == 'SI':
    totalPrice= float(input("Ingrese el total de la compra: $"))
    number= int(input("Ingrese un numero al azar: "))
    if number < 50:
        discount = number * 0.15
        print(f"Usted obtuvo un descuento del %15 -> ${discount}")
    else:
        discount = number * 0.2
        print(f"Usted obtuvo un descuento del %20. -> ${discount}")
    
    follow = input("¿Desea seguir este programa? Escriba 'si', de lo contrario cualquier tecla...\nRespuesta: ")   
    follow = follow.upper() 


