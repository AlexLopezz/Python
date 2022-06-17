'''Ejercicio 9: ¿Un string representan un entero?
En este ejercicio escribirá una función llamada es_entero que determina si los caracteres en una cadena representan un número entero válido.
Al determinar si un string representa un número entero, debe ignorar cualquier espacio en blanco inicial o final.
Una vez que se ignora este espacio en blanco, una cadena representa un número entero si su longitud es al menos 1 y solo contiene dígitos
o si su primer carácter es + o - y el primer carácter va seguido de uno o más caracteres, todos los cuales son dígitos .
Escriba un programa principal que lea una cadena del usuario e informe si representa o no un número entero.
Sugerencia: Puede encontrar los métodos lstrip, rstrip y / o strip para cadenas útiles cuando complete este ejercicio.'''

'''
*lstrip: Es un metodo que devuelve una copia de la cadena con los caracteres iniciales eliminados.
Por defecto(sin parametros) elimina todos los espacios en blanco que halla al inicio del string.

txt = "..,.,ssqwbanana,,,,,ssqqqww....."
y = txt.lstrip(".,sqw")
Salida: banana,,,,,ssqqqww.....

*rstrip: Es un metodo que devuelve una copida de la cadena con los caracteres finales eliminados.
Por defecto(sin parametros) elimina todos los espacios en blancco que halla al final del string.

x= txt.rstrip(",.qsw")
print(x)

*strip: Es un metodo que devuelve una copia de la cadena con los caracteres iniciales y finales eliminados.
Por defecto(sin parametros) elimina todos los espacios iniciales y finales del string.

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

isdigit(): Es un metodo el cual retorna TRUE si el valor que le pasamos es un numero.
'''


def Es_Entero(strnumber):
    isInt= strnumber.strip() #Eliminamos todos los espacios en blancos ya sean al inicio como al final del string.
    
    if len(isInt) >=1: #Comprobamos como dice la consigna: 
        if isInt[0] == '-' or isInt[0] == '+':
            return isInt[1:].isdigit()#Como ya comprobamos el primer digito, ahora toca comprobar los que restan...
        else:
            return isInt.isdigit()#Puede haber la posibilidad de que no haya puesto como primer caracter los signos [- y +]... 

a= '-102'
b='     +105    '
c= '10a2'
d= '-asdada'
e= '23'

print(Es_Entero(a))
print(Es_Entero(b))
print(Es_Entero(c))
print(Es_Entero(d))
print(Es_Entero(e))


