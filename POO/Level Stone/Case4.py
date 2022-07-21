#Create my class Contact: 
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone
    def getEmail(self):
        return self.email

    def setName(self, newName):
        self.name = newName
    def setPhone(self, newPhone):
        self.phone = newPhone
    def setEmail(self, newEmail):
        self.email = newEmail
    
    def editContact(self, name, phone, email):
        self.setName(name)
        self.setPhone(phone)
        self.setEmail(email)

    def __str__(self):
        return f"\nNombre: {self.getName()}\nTelefono: {self.getPhone()}\nEmail: {self.getEmail()}\n"

#Create my class Agenda(book Contact / Diary contact)
class Agenda:
    def __init__(self):
        self.listContact = []
#Add contacts: you just have to pass the contact type object
    def addContact(self, myNewContact):
        self.listContact.append(myNewContact)
        print("Contacto agregado.")
        print(myNewContact)
#Show the Agenda with all contacts.
    def ShowAgenda(self):
        if(len(self.listContact) != 0):
            print("Lista de contactos: ")
            for list in self.listContact:
                print(list)
        else:
            print("No es posible mostrar la lista de contactos, debido a que no hay ningun contacto en la lista.")  
#Find contacts by three ways: name, phone and email:
    def findName(self, strName):
        find = False
        print(f"Contacto/s encontrado/s:")
        for n in self.listContact:
            if(strName == n.getName()):
                print(n)
                find = True
        if(find != True):
            print("No se encontro ningun contacto con ese nombre.")

    def findPhone(self, strPhone):
        find = False
        print("Contacto/s encontrado/s:")
        for p in self.listContact:
            if(strPhone == p.getPhone()):
                print(p)
                find= True
        if(find != True):
            print("No se encontro ningun contacto con ese numero de telefono.")

    def findEmail(self, strEmail):
        find = False
        print("Contacto/s encontrado/s:")
        for e in self.listContact:
            if(strEmail == e.getEmail()):
                print(e)
                find= True
        if(find != True):
            print("No se encontro ningun contacto con ese email.")
    
    def editContact(self, nameContact):
        for n in self.listContact:
            if nameContact == n.getName():
                thisUser= input(f"¿Es este contacto que usted quiere editar?{n}Escriba 'si' si es asi. De lo contrario cualquier tecla...\nRespuesta: ")
                if(thisUser.lower() == 'si'):
                    strName= input("Ingrese el nuevo nombre de contacto: ")
                    strPhone= input("Ingrese el nuevo numero de telefono de contacto: ")
                    strEmail= input("Ingrese el nuevo email de contacto: ")
                    n.editContact(strName, strPhone, strEmail)
                    print("Contacto modificado.")
                    return
            print("No se ha encontrado el contacto con ese nombre.")
#we just let you know that we close the agenda.
    def quitAgenda(self):
        print("Cerrando agenda...")
        return False

#Function menuAgenda:
def menuAgenda(myAgenda):
    def addContact(myAgenda):
            strName= input("Ingrese el nombre del nuevo contacto: ")
            strPhone= input("Ingrese el numero de telefono del nuevo contacto: ")
            strEmail= input("Ingrese el email del nuevo contacto: ")
            newContact = Contact(strName, strPhone, strEmail)
            myAgenda.addContact(newContact)
    def showAgenda(myAgenda):
            myAgenda.ShowAgenda()
    def findContact(myAgenda):
            decision= input("¿Como desea buscar el contacto?\n1.Nombre\n2.Telefono\3.Email\nDecision: ")
            if(decision == "1"):
                strName= input("Ingrese el nombre: ")
                myAgenda.findName(strName)
            elif(decision == "2"):
                strPhone = input("Ingrese el numero de telefono: ")
                myAgenda.findPhone(strPhone)
            elif(decision == "3"):
                strEmail = input("Ingrese el email del contacto a buscar: ")
                myAgenda.findEmail(strEmail)
            else:
                print("Usted no eligio ninguna de las opciones disponibles.")
    def editContact(myAgenda):
        nameContact= input("Ingrese el nombre de contacto a editar: ")
        myAgenda.editContact(nameContact)
    following = True
    while(following):
        print("Bienvenido a su agenda.¿Que desea realizar?")
        decision = input("1.Añadir contacto.\n2.Listar contactos.\n3.Buscar contacto\n4.Editar contacto\n5.Cerrar agenda\nDecision: ")
        if(decision == "1"):
            addContact(myAgenda)
        elif(decision == "2"):
            showAgenda(myAgenda)
        elif(decision == "3"):
            findContact(myAgenda)
        elif(decision == "4"):
            editContact(myAgenda)
        elif(decision == "5"):
            following = myAgenda.quitAgenda()
        else:
            print("No eligio ninguna de las opciones disponibles...\n")
        
#Main
agenda = Agenda()
menuAgenda(agenda)

    







            