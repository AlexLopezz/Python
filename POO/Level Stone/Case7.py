class Producto:
    def __init__(self, codigoBarra, cantidadLitros, precio, marca):
        self.codigoBarra = codigoBarra
        self.cantidadLitros = cantidadLitros
        self.precio = precio
        self.marca = marca

    def getCodigoBarra(self):
        return self.codigoBarra
    def getCantidadLitros(self):
        return self.cantidadLitros
    def getPrecio(self):
        return self.precio
    def getMarca(self):
        return self.marca
    
    def setCantidadLitros(self,cantLitros):
        self.cantidadLitros = cantLitros
    def setPrecio(self, precio):
        self.precio = precio
    def setMarca(self, marca):
        self.marca = marca
    
    def __str__(self):
        return self.getCodigoBarra()  
class AguaMineral(Producto):
    def __init__(self, codigoBarra, cantidadLitros, precio, marca, origen):
        super().__init__(codigoBarra, cantidadLitros, precio, marca)
        self.origen = origen

    def getOrigen(self):
        return self.origen
    def setOrigen(self, origen):
        self.origen = origen
    
    def __str__(self):
        return f"Tipo de producto: {__class__.__name__}\nCodigo de barra: {self.getCodigoBarra()}\nCantidad de litros: {self.getCantidadLitros()}\n"\
            f"Precio: {self.getPrecio()}\nMarca: {self.getMarca()}\nOrigen: {self.getOrigen()}\n-----------------------------------------------------\n"        
class Gaseosa(Producto):
    def __init__(self, codigoBarra, cantidadLitros, precio, marca, porcentajeAzucar, promocion):
        super().__init__(codigoBarra, cantidadLitros, precio, marca)
        self.porcentajeAzucar = porcentajeAzucar
        self.promocion = promocion

    def getPorcentAzucar(self):
        return self.porcentajeAzucar
    def getPromocion(self):
        return self.promocion

    def setPorcentAzucar(self, porcentAzucar):
        self.porcentajeAzucar = porcentAzucar
    def setPromocion(self, promocion):
        self.promocion = promocion
    
    def __str__(self):
        return f"Tipo de producto: {__class__.__name__}\nCodigo de barra: {self.getCodigoBarra()}\nCantidad de litros:{self.getCantidadLitros()}"\
            f"\nPrecio: {self.getPrecio()}\nMarca: {self.getMarca()}\nPorcentaje de azucar: {self.getPorcentAzucar}\nPromocion: {self.getPromocion()} "
class Deposito:
    def __init__(self, nombre):
        self.nombre = nombre
        self.almacen = []

    #Nombre del almacen
    def getNombre(self):
        return self.nombre

    def lengthAlmacen(self):
        return len(self.almacen)

    #Agregar productos
    def addProduct(self, product):
        if len(self.almacen) == 0:
            self.almacen.append(product)
            print("Producto agregado.")
        else:
            for i in self.almacen:
                if product.getCodigoBarra() != i.getCodigoBarra():
                    self.almacen.append(product)
                    print("Producto agregado")
                else:
                    print("Ocurrio un error, no se puede agregar un producto al almacen debido a que tiene el mismo codigo de barra.")
        
    #Eliminar productos        
    def removeProduct(self, CodigoBarra):
        if self.lengthAlmacen() != 0:
            for product in self.almacen:
                if CodigoBarra == product.getCodigoBarra():
                    self.almacen.remove(product)
                    print("Producto eliminado.")
                else:
                    print("No se pudo eliminar el producto, debido a que no se encontraron resultados.")
        else:
            print("No se puede eliminar productos, ya que el almacen no contiene productos.")
    
    #Mostrar informacion
    def showAlmacen(self):
        if len(self.almacen) != 0:
            print("-----Productos actualmente almacenados----")
            for products in self.almacen:
                print(products)
        else:
            print("No hay productos almacenados actualmente.")

    #Calcula el precio de todos los productos
    def totalPriceAllProducts(self):
            total= 0 
            for product in self.almacen:
                total+= product.getPrecio()
            return total
    
    #Calcula el precio total de una marca de bebida.
    def TotalPriceMarcaProducts(self, marca):
            total=0
            for product in self.almacen:
                if marca == product.getMarca():
                    total+=product.getPrecio()
            return total

    #Info del deposito.
    def __str__(self):
        return self.getNombre()
# ------------------------------------------------------------------------- #
def menuAndDecision():
    try:
        decision = int(input("¿Que desea realizar?\n1.Ver productos almacenados\n2.Agregar productos\n3.Eliminar productos"\
        f"\n4.Calcular precio de bebidas almacenadas\n5.Calcular precio de una marca en especifico.\n6.Salir\nDecision: "))
    except:
        print("ERROR: Usted debe ingresar una opcion correcta.(Solo se permite numeros, no caracteres.)\n")
    else:
        return decision
def promocion(strPromocion):
    if strPromocion.lower() == 'si':
        return True
    else: 
        return False
def fillProduct(deposito):
    follow = True
    while(follow):
        tipo = input("¿Que tipo de producto desea registrar en el almacen?\n1.Agua mineral\n2.Gaseosa\nRespuesta: ")
        if tipo == '1':
            try:
                codigoBarra= int(input("Ingrese por favor el codigo de barra del producto: "))
                cantLitros = float(input("Ingrese por favor la cantidad de litros de la bebida: "))
                precio = float(input("Ingrese el precio del producto: $"))
                marca = input("Ingrese la marca del producto: ")
                origen= input("Ingrese el origen del producto(Ciudad, Manantial...etc): ")
                wather = AguaMineral(codigoBarra, cantLitros, precio, marca, origen)
                deposito.addProduct(wather)
            except:
                print("ERROR: Asegurese de completar correctamente los campos de informacion.")
        elif tipo == '2':
            try:
                codigoBarra= int(input("Ingrese por favor el codigo de barra del producto: "))
                cantLitros = float(input("Ingrese por favor la cantidad de litros de la bebida: "))
                precio = float(input("Ingrese el precio del producto: $"))
                marca = input("Ingrese la marca del producto: ")
                porcentajeAzucar= float(input("Ingrese el porcentaje de azucar del producto: %"))
                strPromocion= input("El producto de la gaseosa tiene alguna promocion? (Escriba 'si' si lo tiene, cualquier tecla sino...): ")
                soda = Gaseosa(codigoBarra, cantLitros, precio, marca, porcentajeAzucar, promocion(strPromocion))
                deposito.addProduct(soda)
            except:
                print("ERROR: Asegurese de completar correctamente los campos de informacion.")
        else:
            print("ERROR: Usted no eligio ninguna de las opciones posibles.")
        decision= input("¿Desea volver a intentarlo?(Escriba 'si', si es que desea reintentarlo. Cualquier tecla para no): ")
        if decision.lower() != 'si':
            follow = False
def findAndRemove(deposito):
    codigoBarra= int(input("Ingrese por favor el codigo de barra del producto a eliminar: "))
    deposito.removeProduct(codigoBarra)
def calculateAll(deposito):
    if deposito.lengthAlmacen() != 0:
        total = deposito.totalPriceAllProducts()
        print(f"El precio total de todos los productos es de: ${total}")
    else:
        print("No se puede calcular el precio total, debido a que el almacen no contiene productos.")
def calculateSpecificProduct(deposito):
    if deposito.lengthAlmacen() != 0:
        marca = input("Ingrese por favor la marca del producto: ")
        total = deposito.TotalPriceMarcaProducts(marca)
        if total != 0:
            print(f"El precio total de todos los productos con la marca '{marca}' es de: ${total}")
        else:
            print("ERROR: No se encontraron productos, con esa marca.")
    else:
        print("El almacen no contiene productos.")

#MAIN
decision = 0
nombreAlmacen = input("Ingrese el nombre del almacen: ")
deposito = Deposito(nombreAlmacen)

while(decision != 6):
    print(f"-----BIENVENIDO AL ALMACEN {deposito}-----")
    decision = menuAndDecision()
    if decision == 1:
        deposito.showAlmacen()
    elif decision == 2:
        fillProduct(deposito)
    elif decision == 3:
        findAndRemove(deposito)
    elif decision == 4:
        calculateAll(deposito)
    elif decision == 5:
        calculateSpecificProduct(deposito)
    elif decision == 6:
        print("Este programa finalizara... Gracias por ejecutarlo y probarlo.")
    else:
        print("ERROR: Opcion incorrecta.")


    


 



    

        
        
        
    
    
    
    




    
