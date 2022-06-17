'''Ejercicio 8: Capitalízalo
Muchas personas no usan letras mayúsculas correctamente, especialmente cuando escriben en dispositivos pequeños como teléfonos inteligentes.
En este ejercicio, escribirá una función que capitaliza los caracteres apropiados en una cadena.
Una "i" minúscula debe reemplazarse por una "I" mayúscula si está precedida y seguida de un espacio.
El primer carácter de la cadena también debe estar en mayúscula, así como el primer carácter no espacial después de un ".", "!" o "?" Por ejemplo
si la función se proporciona con la cadena "¿a qué hora tengo que estar allí? ¿cuál es la dirección?" entonces debería devolver la cadena
"¿A qué hora tengo que estar allí? ¿Cuál es la dirección?".
Incluya un programa principal que lea una cadena del usuario, la capitalice utilizando su función y muestre el resultado.'''

def Capitalize(stringg):
    i=0
    resultado=""
    while len(stringg)> i:
        if stringg[i] == 'i' and stringg[i+1] == ' ':
            resultado+= stringg[i].upper()
        elif stringg[i] == '¿' or stringg[i] == '.' or stringg == '!':
            resultado+= stringg[i]+ stringg[i+1].upper()
        else:
            resultado+=stringg[i]
        i+=1
    print(stringg)
        
cadena= "¿hola como estas?"
Capitalize(cadena)    
