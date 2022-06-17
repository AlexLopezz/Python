'''Tres personas deciden invertir su dinero para fundar una empresa.
Cada una de ellas invierte una cantidad distinta.
Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.'''

amountPerson1= float(input("Digite la cantidad de capital invertida de la persona N°1: $"))
amountPerson2= float(input("Digite la cantidad de capital invertida de la persona N°2: $"))
amountPerson3= float(input("Digite la cantidad de capital invertida de la persona N°3: $"))
if amountPerson1>0 and amountPerson2>0 and amountPerson3>0:
	amountTotal= amountPerson1+amountPerson2+amountPerson3

	percetPerson1 = (amountPerson1*100)/amountTotal
	percetPerson2 = (amountPerson2*100)/amountTotal
	percetPerson3 = (amountPerson3*100)/amountTotal

	option=input("¿Desea saber el PORCENTAJE de alguno de los miembros? 's' para si, cualquier tecla para no...")
	if option.lower() == 's':
		option= input("1.PORCENTAJE de la primer persona.\n2.PORCENTAJE de la segunda persona\n3.PORCENTAJE de la tercer persona.\nDecision: ")
		if option == "1":
			print(f"PLata invertida: ${amountPerson1}. PORCENTAJE: %{percetPerson1}")
		elif option == "2":
			print(f"PLata invertida: ${amountPerson2}. PORCENTAJE: %{percetPerson2}")
		elif option == "3": 
			print(f"PLata invertida: ${amountPerson3}. PORCENTAJE: %{percetPerson3}")
		else:
			print("[X]No eligio ninguna opcion.")
	else:
		print("[X]Usted se nego a saber el porcentaje de cada integrante. Adios!")

else: print("->Para saber el porcentaje de las personas que invirtieron, debe ingresar valores mayores a 0.")