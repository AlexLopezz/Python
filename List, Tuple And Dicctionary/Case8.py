''' Construya un algoritmo que sume todos los elementos en posición par de una lista. '''

#Suma total de cada uno de los elementos de la lista: 
def totalList(list): 
    total = 0 #Declaramos e inicializamos una variable, que nos va calcular el totla de la suma de todos los elementos de la lista
    for i in list: #Con este for, recorreremos la lista
        total+= i #El valor de cada elemento sera sumado y almacenado en la variable total.
    return total #Retornamos el valor total de la suma de cada uno de los elementos de la lista.
#Retornara una lista, con la suma total de la lista, en posiciones pares de dicha lista.
def totalPar(list):
    sumTotal = totalList(list) #Almacenamos en una variable, la suma total de la lista.
    for iterable in range(0,len(list)): #Recorremos la lista
        if iterable % 2 == 0: #Si iterable es par entonces: 
            list[iterable] = sumTotal #al contenido de la lista en posicion de iterable, le asginaremos ese valor.
    return list #Retornamos la lista con sus respectivos valores.

#Main

#Creamos una lista con elementos: 
list= [10,20,30,40,50,60,70,80,90,100]
#Dejemos que la funcion totalPar haga su magia: 
list = totalPar(list)
#Imprimimos en pantalla el contenido de la lista: 
print(list)