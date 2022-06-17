'''Escribir un programa el cual lea dos valores enteros.
Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''.
Si el segundo es menor que el primero, que imprima el mensaje ``Abajo''.
Si los números son iguales, que imprima el mensaje ``igual''.
Si alguno de los datos ingresados es igual a 0, que imprima un mensaje conteniendo la palabra ``Error''.'''

follow = 'SI'

while follow == 'SI':
    number = int(input("Ingrese un valor entero: "))
    number2 = int(input("Ingrese un segundo valor entero: "))

    if number == 0 or number2 == 0:
        print("Error")
    elif number == number2:
        print("Igual")
    elif number2 < number:
        print("Abajo")
    elif number < number2:
        print("Arriba")

    follow = input("¿Desea seguir este programa? Escriba 'si', de lo contrario cualquier tecla...\nRespuesta: ")   
    follow = follow.upper() 
