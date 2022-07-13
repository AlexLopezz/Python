import Case1

class Bicicleta(Case1.Vehiculo):
    def __init__(self, tipo,color, rueda):
        super().__init__(color, rueda)
        self.tipo = tipo
        
    def getRueda(self):
        return super().getRueda()
    def getTipo(self):
        return self.tipo

    def setTipo(self, nuevoTipo):
        self.tipo = nuevoTipo
    
    def __str__(self) -> str:
        return __class__.__name__
    
class Motocicleta(Bicicleta):
    def __init__(self, velocidad, cilindrada, tipo, color, rueda):
        super().__init__(tipo, color, rueda)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def getVelocidad(self):
        return self.velocidad
    def getCilindrada(self):
        return self.cilindrada
    def getRueda(self):
        return self.rueda
    def setVelocidad(self, nuevaVelocidad):
        self.velocidad = nuevaVelocidad
    def setCilindrada(self, nuevaCilindrada):
        self.cilindrada = nuevaCilindrada

    def __str__(self):
        return __class__.__name__

class Camioneta(Case1.Coche):
    def __init__(self, velocidad, cilindrada, carga, color, rueda):
        super().__init__(velocidad, cilindrada, color, rueda)
        self.carga = carga
    
    def getRueda(self):
        return self.rueda
    def getCarga(self):
        return self.carga
    def setCarga(self, nuevaCarga):
        self.carga = nuevaCarga
    
    def __str__(self):
        return __class__.__name__

def catalogar(listaVehiculos):
    for v in listaVehiculos:
        print(f"Nombre del vehiculo: {v}")


def catalogarModificado(listaVehiculos, ruedas):
    coincide=0
    for v in listaVehiculos:
        if v.getRueda() == ruedas:
            coincide+=1
    print(f"Se han encontrado {coincide} vehiculos con {ruedas} ruedas.")



vehiculos = []    
#Creamos las subclases:
auto = Case1.Coche(120, 1.8, "Azul", 4)
moto = Motocicleta(120, 110,"Urbana","Negro",2)
bici = Bicicleta("Deportiva","Blanca",2)
camion = Camioneta(120,2.4,650,"Azul",4)

#Agregamos a la lista vehiculos:
vehiculos.append(auto)
vehiculos.append(moto)
vehiculos.append(bici)
vehiculos.append(camion)

catalogar(vehiculos)
catalogarModificado(vehiculos,4)
    

