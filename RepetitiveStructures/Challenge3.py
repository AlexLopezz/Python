'''En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra
llegan a la caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad que lleven en la caja
le entregan un código de descuento que se aplicará sobre el total de su compra.}
Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra. 

*Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; 
si es amarilla un 25% y si es blanca no obtendrá descuento. '''

'''Observacion: 
-> Como no especifica la cantidad de tapitas, pondremos un limite: 
Si llega con 150 tapitas pero menos de 500 el descuento es del %25, en este caso sera el codigo amarillo
Si llega con mas de 500 tapitas el decuento es del %40, en este caso sera el codigo rojo ''' 

isOpenStore = False

answerRequest = input("Antes de comenzar, queria preguntar si, ¿la tienda esta abierta?: Si es asi... Digite 'si', de lo contrario cualquier tecla...\nRespuesta: ")
if answerRequest.lower() == "si":
	isOpenStore = True
	while isOpenStore == True:
		client = input("¿Hay clientes? Digite 'si', de lo contrario.. cualquier tecla\n->Respuesta: ")
		if  client.lower() == "si":
			totalPrice = float(input("Por favor ingrese el precio total de la compra: $"))
			caps = input("¿El cliente trajo tapitas? Si es asi digite 'si', de lo contrario cualquier tecla...\nRespuesta: ")
			if caps.lower() == "si":
				amountCaps = int(input("Por favor ingrese la cantidad de tapitas que trajo el cliente: "))
				if amountCaps > 500:
				    print("Codigo de descuento ROJO.")
				    discountPrice = totalPrice * 0.40
				    totalPrice-= discountPrice
				    print(f"El cliente debe pagar ${totalPrice}, debido a que tiene un %40 de descuento. Ya que trajo un total de {amountCaps} tapitas.")
				elif amountCaps >= 150 and amountCaps < 500:
				    print("Codigo de descuento AMARILLO.")
				    discountPrice = totalPrice * 0.25
				    totalPrice -= discountPrice 
				    print(f"El cliente debe pagar ${totalPrice}, debido a que tiene un %25 de descuento. Ya que trajo un total de {amountCaps} tapitas.")
				else:
					print(f"El cliente debe pagar ${totalPrice}. trajo un total de {amountCaps} pero no obtuvo ningun descuento.")
			else:
				print(f"El cliente debe pagar ${totalPrice}")
		else:
			statuStore = input("¿La tienda sigue abierta?Si es asi... Digite 'si', de lo contrario cualquier tecla...\nRespuesta: ")
			if statuStore != "si":
				isOpenStore = False

print("-> Mensaje de la tienda: Que tengas un buen dia, volve mañana!")
