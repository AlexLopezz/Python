'''Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía pública.
Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5 dígitos
a la Central con el siguiente significado:

3 letras: Correspondientes a la patente.

Del valor numérico:
El 4 número indica
1- Tiró basura a la vía pública
0 - No tiró basura a la vía pública

El 5 número indica
1- Ya había sido multado el vehículo
0 - Vehículo sin multas.

->Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y
porcentaje de éstos que ya habían sido multados. '''
finish = False
trashVehicles = 0
finedVehicles = 0

print("----------------------SISTEMA DE CONTROL DE VEHICULOS----------------")
while finish == False:
	decision = input("Si usted ve que un vehiculo tiro basura: presione 1, de lo contrario cualquier tecla...\nRespuesta: ")
	if decision == "1":
		patent = input("-> Digite las tres letras de la patente: ")
		if len(patent) == 3:
			carSystem = patent+"1" #Tiro basura en la via publica 
			trashVehicles+=1
			carFined = input("¿El carro ya ha sido multado?Si es asi, presione 1 de lo contrario cualquier tecla...\nRespuesta: ")
			if carFined == "1":
				carSystem += "1"
				finedVehicles+=1
				print(f"----------------Numero de 5 digitos generado por el sistema: {carSystem.upper()}-----------------------\n")
			else:
				carSystem += "0"
				print(f"----------------Numero de 5 digitos generado por el sistema: {carSystem.upper()}-----------------------\n")
		else:
			print("[X] No se registrara debido a que no indico las tres letras de la patente. [X]")
	else:
		decision = input("¿Desea terminar la simulacion?: Presione 's' para si, cualquier tecla para no...    ")
		if decision == "s":
			finish = True

percentCarFined = (finedVehicles * 100) / trashVehicles 
print("-------ESTADISTICAS--------")
print(f"-> La cantidad de vehiculos que tiraron basura son/es de: {trashVehicles}")
print(f"-> El porcentaje de vehiculos multados fue de %{percentCarFined}")
