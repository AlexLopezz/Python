'''
Ejercicio 11: ¿Es un número primo?
Un número primo es un número entero mayor que 1 que solo es divisible por uno y por sí mismo.
Escriba una función que determine si su parámetro es primo o no, devolviendo True si lo es y False en caso
contrario.
Escriba un programa principal que lea un número entero del usuario y muestre un mensaje que indique si es primo
o no.
Asegúrese de que el programa principal no se ejecutará si el archivo que contiene su solución se importa a otro programa.'''


def Es_Primo(entero):
    for i in range(2,entero):
        if entero % i == 0:
            return False
    return True

entero= int(input("Ingrese por favor un numero entero para saber si es primo: "))
print(f">El numero {entero} es primo?\nRespuesta de la funcion: {Es_Primo(entero)}")
#print(Es_Primo(33)) Probando si la funcion, funciona en su totalidad.
