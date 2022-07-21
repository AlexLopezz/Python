''' Realizar un algoritmo que invierta el orden de una cola.'''

#2 algoritmos: uno con for (el mas tipico). Otra con while(menos eficiente, pero de igual resultado)

def reverseQueue(queue):
    myQueue = [] #Declaramos una cola sin elementos.
    for i in range(len(queue)): #Iteraremos hasta la longitud de la cola.
        myQueue.append(queue.pop()) #Lo que hacemos aqui es asignar a cada elemento de mi lista, los elementos de la posicion finales de la cola con pop()
    return myQueue

def reverseQueue2_0(queue):
    myQueue = [] #Declaramos una cola, la cual retornaremos
    iterable = len(queue) - 1   #Asignamos la (longitud de la cola - 1) debido a que el 0 cuenta como elemento, por lo tanto habra un elemento de mas...
    
    while(iterable >= 0):  
        myQueue.append(queue[iterable])  #Vamos agregando los elementos finales de la cola pasada por parametro a nuestra lista que antes estaba vacia.
        iterable-=1 #Por cada iteracion restamos 1.
    return myQueue #Retornamos la nueva cola invertida.


#Creamos una cola:  
queue = [10,23,4432,43523,2342,2112312,3242,123,223]
#Como vimos en el caso9, se puede mostrar por pantalla desde el metodo, ya que retorna una lista. Funcionaria como un get.
print(f"Cola con orden invertido: \n{reverseQueue(queue)}")
print(f"Cola con orden invertido: \n{reverseQueue2_0(queue)}")

