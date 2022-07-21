''' Elabore un programa que dada una lista de 15 elementos, copie en otra lista
los elementos pares multiplicados por 2.'''

import random 

def fill_15Elements():
    list = [] #Declaramos una lista vacia
    for i in range(15):
        list.append(random.randint(1,100)) #Agregamos a la lista un valor random entre 1 y 100.
    return list 

def listOdd(list):
    otherList = [] #Declaramos una lista sin elementos.
    for i in list: 
        if i % 2 == 0: #Si el elemento de i es par, entonces:
            otherList.append(i) #Agregamos a la lista
    return otherList #Devolvemos los elementos pares de la lista.

list = fill_15Elements() #Rellenamos la lista con 15 elementos randoms.
print(f"Lista de 15 elementos: \n{list}")

otherList = listOdd(list) #En otra lista, cargaremos los elementos que son pares de x lista...
print(f"Lista extraida con sus elementos pares: \n{otherList}")
#NOTA: Tambien en vez de asignar a una variable, podriamos mostrar directamente listOdd, ya que retorna una lista.