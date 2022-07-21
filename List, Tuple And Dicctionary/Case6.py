class Cola:
    def __init__(self):
        self.cola = list()
    
    def addElement(self,element):
        self.cola.append(element)
    
    def removeElement(self):
        print(f"Elemento eliminado: {self.cola.pop()}")
    
    def isEmpty(self):
        return len(self.cola) == 0
    
    #FUncionaria como un get:
    def returnQueue(self):
        return self.cola
    
myCola = Cola()
print(myCola.isEmpty())
myCola.addElement(2)
print(myCola.isEmpty())

myCola.addElement(12)
myCola.addElement(43)
myCola.addElement(90)
myCola.removeElement()

otraCola = myCola.returnQueue()

print(otraCola)
