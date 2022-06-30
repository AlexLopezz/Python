class Alumno:
    def __init__(self, nombre, apellido, dni, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.sexo = sexo
        self.nota = 0
    
    def mostrarNombreYApellido(self):
        print(self.nombre, self.apellido)
    
    def mostraNombre(self):
        print(self.nombre)
    def modificarNombre(self, nombreNuevo):
        self.nombre = nombreNuevo
    
    def mostrarDNI(self):
        print(self.dni)
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


class Profesor:
    def __init__(self, nombre, apellido, materia):
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia
    
    def mostrarNombreYApellido(self):
        print(self.nombre, self.apellido)

    
    def modificarNombre(self, nombreNuevo):
        self.nombre = nombreNuevo
    
class Aula:
    def __init__(self, profesor, listAlumnos):
        self.profesor = profesor
        self.listAlumnos = listAlumnos

    def cantidadDeAlumnos(self):
        return len(self.listAlumnos)
    
    def __str__(self):
        return 'El aula 2 esta a cargo del profesor {}, quien tiene un total de {} alumnos.'.format(self.profesor.nombre, self.cantidadDeAlumnos())
#MAIN

profesor = Profesor("Nicolas", "Tortosa", "Desarrollo WEB") #Profesor: Nico Tortosa
#Creo 3 objetos de clase Alumno.
alumnoNuevo = Alumno("fulanito","hernndez",13211,"m") 
alumnoNuevo2 = Alumno("marta","martinez",2323,"f")
alumnoNuevo3 = Alumno("jorge","jorgiño",23131,"m")

#print(alumnoNuevo3)
#LISTA DE ALUMNOS.
listAlumnos= []
listAlumnos.append(alumnoNuevo.nombre)
listAlumnos.append(alumnoNuevo2.nombre)
listAlumnos.append(alumnoNuevo3.nombre)

print(listAlumnos)

'''aula2 = Aula(profesor, listAlumnos) #Se creo correctamente el aula2.
print(aula2) '''





