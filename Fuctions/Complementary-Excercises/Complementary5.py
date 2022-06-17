'''Ejercicio 5: De número entero a número ordinal
Las palabras como primero, segundo y tercero se refieren a números ordinales.
En este ejercicio, escribirá una función que toma un número entero como su único parámetro y devuelve una cadena que contiene el número ordinal
apropiado como único resultado.
Su función debe manejar los enteros entre 1 y 12 (inclusive). Debería devolver una cadena vacía si se proporciona un valor fuera de este rango como parámetro.
Incluya un programa principal que utilice su función mostrando cada número entero del 1 al 12 y su número ordinal.'''

def ordinalNumber(number):
    numberOrdinal = ["Primero","Segundo","Terero","Cuarto","Quinto","Sexto","Septimo","Octavo","Noveno","Decimo","Onceavo","Doceavo"]
    return numberOrdinal[(number-1)]

number= int(input("Ingrese un numero natural que no sea mayor a 12: "))
if number <= 12:
    print(f">El numero {number} en ordinal es: {ordinalNumber(number)}")
else:
    print(">Usted no cumplio con la consigna.")
