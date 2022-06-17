''' Ejercicio 1: Triángulos

Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo
como sus parámetros y devuelva la hipotenusa del triángulo, calculada usando el teorema de Pitágoras
como resultado de la función.
Incluya un programa principal que lea las longitudes de los lados más cortos de un triángulo rectángulo
del usuario, use su función para calcular la longitud de la hipotenusa y muestre el resultado.'''

import math
def hipotenusa(sideA, sideB):
    addPow = (sideA*sideA) + (sideB*sideB) #Si se quiere realizar con pow(), se debe sacar la potencia de los dos numeros primero...
    return math.sqrt(addPow)

sideA = float(input("Ingrese por favor el lado A del triangulo rectangulo: "))
sideB = float(input("Ingrese por favor el lado B del triangulo rectangulo: "))
resultHipotenusa= hipotenusa(sideA,sideB)
print(f"La longitud de la hipotenusa es: {resultHipotenusa}")
