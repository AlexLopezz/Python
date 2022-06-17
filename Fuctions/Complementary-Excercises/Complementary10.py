'''
Ejercicio 10: Precedencia del operador
Escriba una función llamada precedencia que devuelve un número entero que representa la precedencia de un
operador matemático. Una cadena que contiene el operador se pasará a la función como su único parámetro.
Su función debe devolver 1 para + y -, 2 para * y /, y 3 para ˆ.
Si la cadena que se pasa a la función no es uno de estos operadores, la función debería devolver -1.

Incluya un programa principal que lea un operador del usuario y muestre la precedencia del operador o un mensaje
de error que indique que la entrada no era un operador.

En este ejercicio, se usa ˆ para representar la exponenciación, en lugar de la elección de Python de **, para facilitar el desarrollo de la solución.'''

def precedencia(strOperator):
    NoBlanksOperaator= strOperator.strip()
    if NoBlanksOperaator == '+' or NoBlanksOperaator == '-':
        return 1
    elif NoBlanksOperaator == '*' or NoBlanksOperaator == '/':
        return 2
    elif NoBlanksOperaator == 'ˆ' or NoBlanksOperaator == '**':
        return 3
    else:
        return -1

def WhatIs(operator):
    if operator == 1:
        print("Es un operador de SUMA(+) o RESTA(-).")
    elif operator == 2:
        print("Es un operador de MULTIPLICACION(*) o DIVISION(/)")
    elif operator == 3:
        print("Es un operador de EXPONENCIA(xˆY o x**Y).")
    else:
        print("[X]No es ningun operador.")
    
strOperator = input("Ingrese por favor un operador: ")
intOperator= precedencia(strOperator)
WhatIs(intOperator)
    