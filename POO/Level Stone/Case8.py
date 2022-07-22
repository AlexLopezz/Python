class Cuenta:
    def __init__(self, titular):
        self.__titular__= titular
        self.__cantidad__= 0
    
    def getTitular(self):
        return self.__titular__
    def getCantidad(self):
        return self.__cantidad__

    def setCantidad(self, cantidad):
        self.__cantidad__ = cantidad
    
    def mostrarInformacion(self):
        print(f"-----Informacion de la cuenta-----\nTitular de la cuenta: {self.getTitular()}\nCantidad en caja: ${self.getCantidad()}")
    
    def ingresarDinero(self,cantidad):
        if cantidad > 0:
            self.setCantidad(cantidad)
    
    def retirarDinero(self, cantidad):
        cantidadARestar = self.getCantidad() - cantidad
        self.setCantidad(cantidadARestar)
    

#MAIN: Se muestra la funcionalidad de la clase cuenta. Aun que tambien se puede realizar un programa completo a prueba de errores.

#Pedimos los datos del titular: 
nombre = input("Ingrese por favor su nombre completo: ")
apellido = input("Ingrese por favor su apellido: ")

cuenta = Cuenta(apellido+" "+nombre)
#Por defecto, la cuenta del titular no tendra nada en caja.(no tendra dinero)
cuenta.mostrarInformacion()
#Podemos agregar dinero. NOTA: Si se ingresa un monto menor a 0, su caja de ahorro quedara con el mismo valor debido a que no es valido monto negativos, tampoco 0.
monto= float(input("Ingrese por favor el monto que desea agregar a su caja de ahorro: $"))
cuenta.ingresarDinero(monto)
#Se puede retirar dinero. NOTA: Este programa no tiene control sobre numeros rojos. es decir, si su caja de ahorro esta con numeros negativos(deuda).
monto= float(input("Ingrese por favor el monto que desea retirar de su caja de ahorro: $"))
cuenta.retirarDinero(monto)

#Verificamos que se han realizado los cambios: 
cuenta.mostrarInformacion()