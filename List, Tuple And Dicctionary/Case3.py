''' Escriba un algoritmo que permita cargar una lista.
Y que luego, una vez cargada, controle y sustituya cualquier elemento negativo por 0.'''

#Importamos random, ya que lo necesitaremos para realizar el algoritmo.
import random

#Definimos 2 funciones, una para verifar si algun elemento de la lista tiene valor negativo. Y otra para rellenar la lista.
def ListNotNegative(aList):
    for iterable in range(0,len(aList)): #Iteraremos toda la lista con este for.
        if aList[iterable] < 0: #Verificamos cada elemento si es menor a 0.
            aList[iterable] = 0 #Si lo es, entonces modificamos su valor a 0, como nos indica la consigna
    print(aList) #Mostramos por pantalla como nos indica la consigna

#Aqui esta la utilidad de la libreria Random. 
def fillList(aList):
    for i in range(0, random.randint(5,15)): #La longitud, lo determino con randint, para que almenos tenga 5 elementos y como mucho 15.
        aList.append(random.randint(-500, 500)) #Agregamos a la lista un numero random entre -500 y 500...
    return aList #Cuando sale del for, retornamos la lista rellena con elementos random-


#Main. 

listDefault = [] #Creamos una lista vacia 
listDefault = fillList(listDefault) #La rellenamos con nuestra funcion, y la recibimos en la misma variable
ListNotNegative(listDefault) #Invocamos a la otra funcion que haga su magia.



