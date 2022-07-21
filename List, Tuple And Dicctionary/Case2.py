'''Haz un programa que almacene 5 elementos en una variable del tipo lista,
la modiﬁque para que cada componente sea igual al cuadrado del componente original.
El programa mostrara la lista resultante por pantalla. '''

def powList(aList):
    for i in range (0,len(aList)):
        aList[i] = pow(aList[i],2) #Tambien se podria realizar de esta manera: aList[i] = aList[i]*aList[i]
    print(aList)

#Creamos la lista.
lista = []
#Agregamos los 5 elementos: 
lista.append(2)
lista.append(6)
lista.append(3)
lista.append(2)
lista.append(4)

#Una vez agregado los 5 elementos a la lista, invocamos a powList que haga su magia:
powList(lista)




