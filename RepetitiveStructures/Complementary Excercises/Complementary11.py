'''Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado.'''

follow= 'SI'
while follow == 'SI':
    number= int(input("Ingrese un numero por favor: "))
    for i in range(1,number):
        if number % i==0:
            print(f"-> El numero {i} es divisor de {number}")

    follow= input("¿Desea seguir?Escriba 'SI'... De lo contrario, cualquier tecla.")
    follow= follow.upper()

