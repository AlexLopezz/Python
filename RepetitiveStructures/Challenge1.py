'''Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados
para el ambiente.

a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa
debe preguntar al usuario la contraseña, y no le permita continuar hasta que la haya ingresado
correctamente.

b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. '''

#a) 
valid = False
password = input("-> Por favor, ingrese su contraseña: ")
print("[Check] Muy bien, la contraseña generada se guardo correctamente.")
print("------------------------Simulacion de Login---------------------------")

while valid == False:
	verifyPass = input("-> Por favor, ingrese la contraseña que guardo en este programa: ")
	if verifyPass == password:
		print("[Check] Muy bien, se logeo exitosamente!")
		valid = True
	else:
		print("[X] ERROR!. La contraseña que usted ingreso no coincide con la que guardo anteriormente.")

print("------------------------Simulacion de Login terminada--------------------\n")

#b)
password = input("Por favor ingrese su contraseña: ")
print("Contraseña guardada exitosamente.")
print("------------------------Simulacion de Login con solo 3 intentos---------------------")
intentos = 3

while intentos > 0:
	verifyPass = input("-> Por favor, ingrese la contraseña que guardo en este programa: ") 
	if verifyPass == password:
		print("[Check] Muy bien, se logeo exitosamente")
		break
	else:
		print("[X] ERROR!. La contraseña que usted ingreso no coincide con la que guardo anteriormente.")
		intentos-=1
		if intentos == 0:
			print("Ya no te quedan mas intentos. Adios!")
		else:
			print(f"Te quedan {intentos} intento/s.")

print("-------------------------Simulacion de Login terminada------------------------------")
		
	
