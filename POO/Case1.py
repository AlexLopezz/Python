class Vehiculo:
    def __init__(self, color, rueda):
        self.color = color
        self.rueda = rueda
    
    def getColor(self):
        return self.color
    def getRueda(self):
        return self.rueda

    def setColor(self, nuevoColor):
        self.color = nuevoColor
    def setRueda(self, nuevaRueda):
        self.rueda = nuevaRueda
    
    def __str__(self):
        return __class__.__name__

    
class Coche(Vehiculo):
    def __init__(self,velocidad,cilindrada, color, rueda):
        super().__init__(color, rueda)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    #Implementacion de getters  : Los getters retornan el valor que tienen los atributos.  
    def getRueda(self):
        return self.rueda
    def getColor(self):
        return self.rueda
    def getCilindrada(self):
        return self.cilindrada
    def getVelocidad(self):
        return self.velocidad
    
    #Implementacion de setters  : Los setters modifican el valor de los atributos.
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    def setColor(self, color):
        self.color = color
    def setCilindrada(self, cilindrada):
        self.cilindrada = cilindrada
    def setRueda(self, rueda):
        self.rueda = rueda
    
    def __str__(self):
        return __class__.__name__
'''
auto = Coche(120, 650) #Instanciamos un objeto Coche, con nombre auto e inicializamos sus atributos.
v = Vehiculo() #Instanciamos un objeto Vehiculo. Internamente tiene atributos inicializados.

#Verificamos si la velocidad del auto, es la misma la cual inicializamos:
print(auto.getVelocidad()) 
#Cambiaremos la velocidad establecida inicialmente: 
auto.setVelocidad(220)
#Verificamos si los cambios se hicieron:
print(auto.getVelocidad())

#Dos (2) formas de cambiar el valor de los atributos atraves de los setters:
#1
auto.color= "Azul"
#Verificamos si se cambio el valor del atributo color del objeto auto:
auto.getColor()
#2
auto.setColor("Verde")
#Verificamos si se cambio el valor del atributo color del objeto auto:
auto.getColor()
print(v)
print(auto)
'''






