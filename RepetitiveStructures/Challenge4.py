'''Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado.
Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6 

Aun no tengo habilidades y tampoco se si se puede imprimir colores XD en Python... pero haremos lo siguiente:
le diremos de cuanto de largo y alto quiere el tablero el usuario y despues, en el campo verde digitaremos 
el caracter 'v' y en el blanco la letra 'b'. '''

import numpy as np
large = int(input("Ingrese por favor el largo del tablero: "))
tall = int(input("Ingrese por favor el alto del tablero: "))

print(f"\n---------------------Tablero ecologico de {large}x{tall}------------------")
tablero = np.zeros((tall, large), dtype=str)
tablero[0::2, ::2] = "v" #Desde la fila 0, con saltos de 2 en 2, que tome todas las columnas de dos en dos..
tablero[1::2, ::2] = "b" #Desde la fila 1 hasta el final, con saltos de 2 en 2, que tome todas las columnas de dos en dos..

tablero[0::2, 1::2] = "b" #Desde la fila 0 con saltos de 2 en 2, que tome todas las columnas a partir de la columna 1 de dos en dos..
tablero[1::2, 1::2] = "v" #Desde la fila 1 con saltos de 2 en 2, que tome todas las columnas a partir de la columna 1 de dos en dos..

print(tablero)
