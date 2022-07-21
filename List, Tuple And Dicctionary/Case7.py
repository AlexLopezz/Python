''' Cargar dos listas con la misma cantidad de elementos.
Luego mezclarlas, cargándolas ordenadas en otra lista.'''
def concatList(list, list2): #Nos debera pasar las dos listas para concatenarlas
    anotherList= [] #Creamos una lista
    anotherList.extend(list + list2) #Rellenamos la lista con el metodo extend() el cual concatenara las dos listas pasadas por parametros.
    anotherList.sort() #Luego con la funcion sort() ordenamos, por defecto de orden menor a mayor. Si se quiere ordenar inversamente: anotherList.sort(reverse= True)
    return anotherList #retornamos la lista resultante.


#MAIN.

#Creamos dos listas, con la misma cantidad de elementos: 
list = [2,6,12]
myList = [4,1,15]

#En la variable listResult, obtenemos la lista ordeanada a traves de la funcion concatList: 
listResult = concatList(list, myList)
print(listResult) #Mostramos por pantalla la lista resultante.
