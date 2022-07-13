class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def getNombre(self):
        return self.nombre
    def getTelefono(self):
        return self.telefono
    def getEmail(self):
        return self.email

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre
    def setTelefono(self, nuevoTelefono):
        self.telefono = nuevoTelefono
    def setEmail(self, nuevoEmail):
        self.email = nuevoEmail
    
    def __str__(self):
        return f"Nombre de Contacto: {self.nombre}\nTelefono: {self.telefono}\nEmail: {self.email}"

class Agenda:
    def __init__(self):
        self.listContactos=[]
        self.seguir = True
    
    def menu(self):
        while(self.seguir != False):
            print("¿Que desea realizar?")
            decision = int(input("1.Añadir contacto\n2.Listar contactos\n3.Buscar contacto\n4.Editar contacto\n5.Cerrar agenda\nDecision: "))
            if(decision == 1):
                strNombre = input("Ingrese por favor el nombre de la persona que quiera agregar a su agenda: ")
                strTelefono = int(input("Ingrese por favor el telefono de la persona: "))
                strEmail = input("Ingrese por favor el correo de la persona: ")
                contactoNuevo = Contacto(strNombre, strTelefono, strEmail)
                self.AñadirContacto(contactoNuevo)

            elif(decision == 2):
                print("Contactos existentes: ")
                for listar in self.listContactos:
                    print(listar)

            elif(decision == 3):
                decision= int(input("¿Como desea buscar al contacto?\n1.Por nombre\n2.Por telefono\n3.Por email\nDecision: "))
                if(decision == 1):
                    strNombre = input("Ingrese el nombre de la persona: ")
                    self.BuscarContacto(strNombre)
                elif(decision == 2):
                    intTelefono = int(input("Ingrese el numero del contacto: "))
                    self.BuscarContacto("",intTelefono)
                elif(decision == 3):
                    strEmail = input("Ingrese el email de la persona: ")
                    self.BuscarContacto("",0,strEmail)
                else:
                    print("Usted no eligio ninguna de las opciones disponibles.")
            
            elif(decision == 4):
                nombreBuscar=input("Ingrese el nombre de contacto a editar: ")
                decision = int(input("¿Que datos de contacto desea editar?\n1.Nombre\n2.Telefono\n3.Email\nDecision: "))
                
                if(decision == 1):
                    nombreNuevo = input("Ingrese el nuevo nombre de contacto: ")
                    self.EditarContacto(nombreBuscar, nombreNuevo)
                elif(decision == 2):
                    telefonoNuevo = input("Ingrese el nuevo telefono: ")
                    self.EditarContacto(nombreBuscar,"",telefonoNuevo)
                elif(decision == 3):
                    emailNuevo = input("Ingrese el nuevo email: ")
                    self.EditarContacto(nombreBuscar, "", 0, emailNuevo)
                else:
                    print("Usted no eligio ninguna opcion disponible.")
            
            elif(decision == 5):
                print("Agenda cerrada.")
                seguir = False

    def AñadirContacto(self, contactoNuevo):
        self.listContactos.append(contactoNuevo)
        print("Contacto añadido.")
    
    def BuscarContacto(self, nombre ="", telefono = 0, email=""):
        if(nombre != ""):
            for n in self.listContactos:
                if(n.getNombre() == nombre):
                    return n
                print("No se encontro el contacto.")
                return False
        elif(telefono != 0):
            for t in self.listContactos:
                if(t.getTelefono() == telefono):
                    print("¡Contacto encontrado!")
                    print(n)
                    return t
                print("No se encontro el contacto.")
                return False        
        elif(email != ""):
            for e in self.listContactos:
                if(e.getEmail() == e):
                    print("¡Contacto encontrado!")
                    print(n)
                    return e
                print("No se encontro el contacto.")
                return False

    def EditarContacto(self, nombreContacto, editarNombre="", editarTelefono=0, editarEmail=""):
        if(len(self.listContactos) != 0):
            if(self.BuscarContacto(nombreContacto) != False):
                editarContacto = self.BuscarContacto(nombreContacto)
                if(editarNombre != ""):
                    editarContacto.setNombre = editarNombre
                elif(editarTelefono != 0):
                    editarContacto.setTelefono = editarTelefono
                elif(editarEmail!=""):
                    editarContacto.setEmail = editarEmail

miAgenda = Agenda()
miAgenda.menu()


            