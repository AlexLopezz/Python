'''En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología.
El presupuesto anual del hospital se reparte conforme a la sig. tabla:

ÁREA 		    PORCENTAJE

Pediatría			60%

Traumatología		20%

Kinesiología	    20%

Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal que se ingrese por teclado. '''

budgetEstimate= float(input("[?]Ingrese por favor el PORCENTAJE anual: "))
if budgetEstimate > 0:
	pedriaticArea = budgetEstimate * 0.60
	traumaArea = budgetEstimate * 0.20
	kinesiologyArea= traumaArea 

	print("¿Cual es la area en la que desea saber el monto recibido segun el monto presupuestal?")
	print("1.Pediatria\n2.Traumatologia\n3.Kinesiologia")
	option = int(input("->Decision: "))
	if option == 1:
		print(f"->El area de Pediatria recibio un total de ${pedriaticArea}. que equivale al 60% del monto presupuestal.")
	elif option == 2:
		print(f"->El area de Traumatologia recibio un total de ${traumaArea}. que equivale al 20% del monto presupuestal.")
	elif option == 3:
		print(f"->EL area de Kinesiologia recibio un total de ${kinesiologyArea}. que equivale al 20% del monto presupuestal.")
	else: 
		print("[X]Usted no eligio ninguna opcion presentada anteriormente...")
else: 
	print(f"[X]No se puede calcular la cantidad dinera destinada a las areas, debido a que su monto es de ${budgetEstimate}(debe ser mayor a 0, por lo menos)")
