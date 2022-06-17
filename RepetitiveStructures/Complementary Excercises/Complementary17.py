'''Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si
este se le asigna como un porcentaje de su salario mensual que depende de su antigüedad
en la empresa de acuerdo con la sig. tabla:

Tiempo												Utilidad
Menos de 1 año								      5% del salario

Más de 1 año y hasta 2 años		                  7% del salario

Más de 2 años y hasta 5 años                      10% del salario

Más de 10 años								      20% del salario'''

from ctypes import util


follow = 'SI'
totalUtility=0
while follow == 'SI':
    utility= int(input("Ingrese el tiempo de antiguedad que tiene el trabajador: "))
    if utility == 10:
        totalUtility= (utility * 100) / 20
    elif utility > 2 and utility < 5:
        totalUtility= (utility * 100) / 10
    elif utility > 1 and utility < 2:
        totalUtility= (utility * 100) / 7
    elif utility < 1:
        totalUtility= (utility * 100) / 5
    
    print(f"El reparto anual de utilidades para el trabajador es de: ${totalUtility}")
    follow = input("¿Desea seguir este programa? Escriba 'si', de lo contrario cualquier tecla...\nRespuesta: ")   
    follow = follow.upper()