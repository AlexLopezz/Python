'''Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio.
Debe diseñar un programa que permita monto por cliente y el total recaudado por la gasolinera
tomando en cuenta lo siguiente:
• El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60
• El programa finaliza cuando se introduce una D como tipo de gasolina. '''

amountTotal=0
typeOfClient=""

while typeOfClient != 'D':
    typeOfClient= input("¿Que tipo de cliente es?\nTIPO A = 1L $50\nTIPO B = 1L $55\nTIPO C = 1L $60\nRespuesta: ")
    typeOfClient= typeOfClient.upper()
    if typeOfClient == 'A':
        print("El precio a pagar por el cliente es de $50.")
        amountTotal+= 50
        print("SUCCESS!")
    elif typeOfClient == 'B':
        print("El precio a pagar por el cliente es de $55")
        amountTotal+= 55
        print("SUCCESS!")
    elif typeOfClient == 'C':
        print("El precio a pagar por el cliente es de $60.")
        amountTotal+= 60
        print("SUCCESS!")
    elif typeOfClient != 'D':
        print("ERROR! Cliente no registrado.")
    

print(f"Total recaudado: ${amountTotal}")
