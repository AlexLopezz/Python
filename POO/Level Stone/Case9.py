from msilib.schema import ListBox
from operator import attrgetter
class Libro:
    def __init__(self, titulo, autor, nPaginas, calif):
        self.__titulo__ = titulo
        self.__autor__ = autor
        self.__nPaginas__= nPaginas
        self.__calif__ = calif

    def getTitulo(self):
        return self.__titulo__
    def getAutor(self):
        return self.__autor__
    def getNPaginas(self):
        return self.__nPaginas__
    def getCalif(self):
        return self.__calif__
    
    def __str__(self):
        return f"TITULO LIBRO: {self.getTitulo()}\nAUTOR LIBRO: {self.getAutor()}\nN° PAGINAS LIBRO: {self.getNPaginas()}\nCALIF: {self.getCalif()}\n"
    

class ConjuntoLibros:
    def __init__(self):
        self.conjuntoLibros= []

    def agregarLibro(self, libroNuevo):
        self.conjuntoLibros.append(libroNuevo)

    def eliminarLibro(self, titulo=None, autor=None):
        find = False
        if titulo != None:
            for libro in self.conjuntoLibros:
                if titulo == libro.getTitulo():
                    print(f"Libro removido: {libro}")
                    self.conjuntoLibros.remove(libro)                    
                    find = True
            if find == False:
                print("ERROR: No se encontraron resultados.")
        elif autor != None:
            for libro in self.conjuntoLibros:
                if autor == libro.getAutor():
                    print(f"Libro removido: {libro}")
                    self.conjuntoLibros.remove(libro)
                    find = True

            if find == False:
                print("ERROR: No se encontraron resultados.")
        
    def librosCalif(self):
        listMayorAMenor = sorted(self.conjuntoLibros, key= attrgetter('__calif__'), reverse= True)
        for libro in listMayorAMenor:
            print(libro)

    def mostrarLibros(self):
        for libro in self.conjuntoLibros:
            print(libro)



librosFav = ConjuntoLibros()
l1 = Libro("Caperucita Roja", "Alan Poe", 26, 7)

librosFav.agregarLibro(l1)

librosFav.agregarLibro(Libro("Las mil y una noche", "Sherazade", 40, 9))
librosFav.agregarLibro(Libro("La biblia", "Alan Poe", 110, 10))
librosFav.agregarLibro(Libro("Cuentos de Terror para Franco", "Hugo Mitoire", 90, 7))
librosFav.agregarLibro(Libro("Nuestra parte de noche", "Mariana Enriquez", 80, 8))
librosFav.agregarLibro(Libro("The Enigma", "Joel Dicker", 300, 6))

librosFav.eliminarLibro("The Enigma",None)
librosFav.eliminarLibro(None,"Alan Poe")


#librosFav.librosCalif()   
librosFav.mostrarLibros()

    
