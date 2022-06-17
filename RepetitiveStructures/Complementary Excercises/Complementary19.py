'''Dados los datos de un municipio: zona, sexo y edad de cada uno de sus habitantes, encontrar:

a) porcentaje de varones menores de 15 años para cada zona

b) porcentaje de varones menores de 15 años para todo el municipio

Los datos vienen ordenados por zona.Con dato de zona igual a 0, se indica el fin.'''

percentManLessThanFiveteen=0
follow = 'SI'
while follow == 'SI':
    zone = input("Ingrese la zona donde vive: ")
    if zone == '1':
        percentManLessThanFiveteen+=1
    
    
    
    follow = input("¿Desea seguir este programa? Escriba 'si', de lo contrario cualquier tecla...\nRespuesta: ")   
    follow = follow.upper()