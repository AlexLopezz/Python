'''GESTION DE DONACIONES'''
import datetime 

class Producto:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getCantidad(self):
        return self.cantidad
    def setNombre(self, cantidad):
        self.cantidad = cantidad

    def Calcular(self, cantidad, entidad):
        pass


class Perecedero(Producto):
    def __init__(self, diasCaducar):
        self.diasCaducar = diasCaducar

    def Calcular(self, cantidad, entidades):
        if self.diasCaducar > 0 and self.diasCaducar < 10:
            fecha = datetime.datetime.now 
        else:
            fecha = datetime.datetime.now() + datetime.timedelta(days=7)
        
        promedio = cantidad // entidades
        
        print(f"La cantidad de productos que se le enviara a cada entidad es de: {promedio}")
        print(f"Fecha de entrega es: {fecha.strftime('%d/%m/%Y')}")
        
class NoPerecedero(Producto):
    def __init__(self, tipo):
        self.tipo = tipo
    
    def Calcular(self, cantidad, entidades):
        promedio = cantidad // entidades
        fecha = datetime.datetime.now() + datetime.timedelta(days=30)
        print(f"->Se entregaran para cada entidad un total de {promedio} productos.")
        print(f"->Fecha de entrega: antes del {fecha.strftime('%d/%m/%Y')}")

        
verduras = Perecedero(15)
verduras.Calcular(60,15)

arroz = NoPerecedero("pasta")
arroz.Calcular(500,30)