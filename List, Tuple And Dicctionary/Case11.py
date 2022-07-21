'''Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda
y no en la primera.'''

def updateListElements(listToModify, list): #Pasamos por parametros la lista a modificar y la segunda lista
    for i in range (len(list)): #Recorremos la segund lista
        if list[i] not in listToModify: #si el contenido de la segunda  lista no se encuentra en toda la lista a modificar
            listToModify.append(list[i]) #Agregamos a la lista a modificar.
    listToModify.sort() #La ordenamos, para que sea mas visible los cambios.
    return listToModify #Retornamos la primer lista actualizada.

#MAIN
#Creamos las dos lista.
myList = [2,4,6,8,10,12,14,16,18,20]
myList2 = [3,6,9,12,15,18,21,24,27,30]

print(updateListElements(myList, myList2))

