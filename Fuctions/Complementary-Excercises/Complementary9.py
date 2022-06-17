'''Ejercicio 9: ¿Un string representan un entero?
En este ejercicio escribirá una función llamada es_entero que determina si los caracteres en una cadena representan un número entero válido.
Al determinar si un string representa un número entero, debe ignorar cualquier espacio en blanco inicial o final.
Una vez que se ignora este espacio en blanco, una cadena representa un número entero si su longitud es al menos 1 y solo contiene dígitos
o si su primer carácter es + o - y el primer carácter va seguido de uno o más caracteres, todos los cuales son dígitos .
Escriba un programa principal que lea una cadena del usuario e informe si representa o no un número entero.'''

import random
l1 = []
l2= []
for i in range(10):
    l1.append(random.randint(1,10))
    l2.append(random.randint(1,10))

print(l1)
print(l2)

for it in l2:
    if it not in l1:
        l1.append(it)

print(l1)

                    