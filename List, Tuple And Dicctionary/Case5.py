''' Cargar m elementos en una pila, y luego copiarlos en una nueva lista. '''

class Pila:
    def __init__(self):
        self.pila=[]
    
    def isEmpty(self):
        return len(self.pila) == 0

    def stack(self,element):
        self.pila.append(element)
        print(f"Elemento agregado: {element}")
        print(self.pila)
    
    def returnPila(self):
        return self.pila

    def unstack(self):
        print(f"Elemento borrado: {self.pila.pop()}")
        if not self.isEmpty():
            print(f"Lista actual: {self.pila}")
        else:
            print("Lista sin elementos.")
    
    
myPila = Pila()
print(myPila.isEmpty()) #Esta vacia en este momento. Devolvera false.
#Agreamos elementos a la lista: 
myPila.stack(2)
myPila.stack(4)
myPila.stack(6)
myPila.stack(8)

print(myPila.isEmpty()) #Ya no estaria vacia. Por lo que daria true.
myPila.unstack() #Eliminara el ultimo elemento de la fila.

otraPila = myPila.returnPila()
print(otraPila)