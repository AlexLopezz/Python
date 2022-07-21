'''
Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos,
imprimir el valor del lado con un tamaño mayor y el tipo de triángulo
que es (equilátero, isósceles o escaleno). ''' 

class Triangulo:
    def __init__(self,lado,lado2,lado3):
        self.lado = lado
        self.lado2 = lado2
        self.lado3 = lado3
    
    def setLado(self, lado):
        self.lado = lado
    def setLado2 (self, lado2):
        self.lado2 = lado2
    def setLado3(self, lado3):
        self.lado3 = lado3
    
    def getLado(self):
        return self.lado
    def getLado2(self):
        return self.lado2
    def getLado3(self):
        return self.lado3
    
    def tipoTriangulo(self):
        if self.lado != 0 and self.lado2 != 0 and self.lado3 != 0:
            if self.lado == self.lado2 and self.lado == self.lado3:
                print("El tipo de Triangulo es Equilatero.")
            elif self.lado == self.lado2 and self.lado != self.lado3 or self.lado2 == self.lado3 and self.lado2 != self.lado or self.lado3 == self.lado and self.lado3 != self.lado2:
                print("El tipo de Triangulo es Isosceles.")
            else:
                print("El tipo de Triangulo es Escaleno.")
        else:
            print("No se puede definir el tipo de triangulo debido a dos motivos:")
            print("1. Los lados no estan inicializados.\n2.ALguno de los rectangulos tienen 0 como valor.")
        
    def ladoMayor(self):
        if(self.lado > self.lado2 and self.lado > self.lado3):
            return self.lado
        elif(self.lado2 > self.lado and self.lado2 > self.lado3):
            return self.lado2
        else:
            return self.lado3
        

t = Triangulo(20,15,20)
t.tipoTriangulo()
print(t.ladoMayor())