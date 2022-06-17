'''Ejercicio 6: Centrar una cadena en la terminal

Escriba una función que tome una cadena de caracteres como primer parámetro y el ancho de la terminal en caracteres
como segundo parámetro.
Su función debe devolver una nueva cadena que consta de la cadena original y el número correcto de espacios iniciales
para que la cadena original aparezca centrada dentro del ancho proporcionado cuando se imprima.
No agregue ningún carácter al final de la cadena. Incluya un programa principal que use su función.'''

def solution(caracter, anchor=114):
    espaciosEnBlanco = " "
    longitudCaracter = len(caracter)
    midCMD = (anchor - longitudCaracter) // 2 #Aqui lo que hicimos fue restar la longitud del CMD con la cantidad de caracteres del texto.
                                              #Y luego dividirlo en dos, para que se fije en la mitad.
    espaciosEnBlanco= (espaciosEnBlanco*midCMD)+caracter

    return espaciosEnBlanco
    
    '''Otra forma de realizar:
    for it in range(0,intCMD):
        espaciosEnBlanco+=" "
    espaciosEnBlanco+=caracter '''
    
caracter = input("Por favor ingrese un texto: ")
caracter=solution(caracter)
print(f"{caracter}")
