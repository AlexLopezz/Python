'''Ejercicio 4: Mediana de tres valores
Escriba una función que tome tres números como parámetros y devuelva el valor medio de esos parámetros como resultado.
Incluya un programa principal que lea tres valores del usuario y muestre su mediana.'''

def mediaTresValores(number, number2, number3):
    if number > number2 and number > number3: #Numero1 mas grande
        if number2 > number3: #Numero2 es el valor mediano de los tres valores...
            return number2
        else: #Numero3 es el valor mediano de los tres valores...
            return number3
    if number2 > number and number2 > number3: #Numero2 mas grande.
        if number > number3: #Numero1 es el valor medianos de los tres valores...
            return number
        else:
            return number3 #Numero3 es el valor mediano...
    if number3 > number and number3 > number2:
        if number > number2:
            return number
        else:
            return number2

number1 = int(input("Ingrese el valor del numero 1: "))
number2 = int(input("Ingrese el valor del numero 2: "))
number3 = int(input("Ingrese el valor del numero 3: "))
print(f"El valor mediano de los tres numeros es: {mediaTresValores(number1, number2, number3)}")
