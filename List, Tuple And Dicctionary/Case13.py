'''Leer una frase y luego invierta el orden de las palabras en la frase.
Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en
“palabras mil por vale imagen una”.'''

def reversePalabras(stringPhrase):
    listAux = stringPhrase.split(' ') #Creamos una lista a partir de un string.
    phraseInvert = listAux[::-1] #De esta manera, podemos invertir la lista.
    stringPhrase= ' '.join(phraseInvert) #Cada vez que se coloca un elemento de la lista, se separa por una ' '.
    return stringPhrase #Retornamos en string.

phrase = 'una imagen vale por mil palabras'
print(reversePalabras(phrase))

