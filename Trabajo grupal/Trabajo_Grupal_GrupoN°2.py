'''Realizar una agenda, que se pueda guardar nombre y teléfono.'''

agenda= {} #Guardaremos todos los contactos a traves de un diccionario.
follow= 'SI' #Por defecto, tendremos esta variable que iniciara nuestro bucle.
flag= False #Flag, se lo denomina asi para saber si se cumplio un objetivo dentro del codigo(almenos asi lo uso yo)


#si encontramos un contacto, el flag se volvera True, por lo que si el usuario quiere volver a buscar otro usuario, el flag se quedara siempre en True. Hay que resetearlo
def reset(flag): 
    flag= False

def SaveContact(): #Con esta funcion, guardaremos cada contacto que el usuario me ingrese.
    name= input(">Ingrese por favor el nombre del contacto a agendar: ")
    phone= int(input(">Ingrese por favor el numero de telefono: "))
    agenda[name]= phone
    print("¡Contacto agendado!")

def FindContact(): #Con esta funcion, buscaremos ya sea por nombre o por numero de telefono al contacto deseado...
    if len(agenda)!=0: #Muy importante, siempre verificar si la agenda tiene o no contactos...
        decision= input("¿Como desea buscar al contacto?\n1.Por su nombre\n2.Por su numero de telefono\n>Respuesta: ")
        if decision == '1': #Si el usuario me ingresa uno, entonces...
            name= input(">Ingrese por favor el nombre del contacto: ")
            FindForName(name) #Le pedimos al usuario que ingrese el nombre del contacto, y le pasamos como parametros a mi funcion FindForName...
        elif decision == '2':
            phone= int(input(">Ingrese por favor el numero de telefono del contacto buscado: "))
            FindForPhone(phone) #Una vez que el usuario me ingresa el numero de telefono del contacto, le pasamos por parametros a FindForPhone...
    else:
        print("[X]Disculpe, actualmente usted no tiene ningun contacto en su agenda.") #Si no ingresa la opcion correcta le avisamos...
####

def FindForName(name):
    for n,phone in agenda.items(): #Aqui buscamos en el diccionario el nombre ingresado por el usuario...
        if name == n: #Si el nombre ingresado es el mismo que n(vendria a ser la clave del primer elemento de la agenda..luego el segundo y asi...)
            print(f">¡Contacto encontrado!\nNombre: {n}\nTelefono: {phone}") #Le mostramos al usuario la informacion del usuario agregado a la agenda.
            flag= True #Activamos el flag, debido a que encontramos el usuario...
    if flag != True: #Si en todo el recorrido del diccionario no encontro ninguna clave que sea igual al nombre ingresado por el usuario
        print("[X]Contacto no encontrado.\nMotivos:\nEl contacto no existe.\nQuizas escribio mal el nombre.") #El flag queda en su mismo estado inicial(es decir False.)
    reset(flag) #Aqui es importante invocar al reset para el flag, debido a que si encontro un contacto, l flag siempre quedara en true.

def FindForPhone(phone): #Similar a la funcionalidad de FindForName.
    for n, p in agenda.items():
        if phone == p: #Aqui lo que cambia es que buscamos por el valor, no por la clave...
            print(f">¡Contacto encontrado!\nNombre: {n}\nTelefono: {p}")
            flag= True 
    if flag != True:
        print("[X]Contacto no encontrado.\nMotivos:\nEl contacto no existe.\nQuizas escribio mal el nombre.")
    reset(flag) #Mismo procedimiento a la funcion FindForName.

#Aqui empezaria el 'main' o lo que se mostraria por la consola cmd... Basicamente esta compuesto por menus, que dependen de lo que el usuario le indique..
while follow == 'SI': #Por defecto, siempre entra al bucle. debido a que follow tiene como valor 'SI'
    decision= input("¿Que desea realizar?\n1.Agendar un contacto\n2.Buscar un contacto.\nRespuesta: ")
    if decision == '1': #Si la decision es 1---
        SaveContact() #Entonces invocamos a SaveContact() y que haga su magia..
    elif decision == '2':
        FindContact() #Lo mismo aqui, si el usuario ingresa 2, invocamos a FindContact() que haga su magia
    else:
        print("Usted no ingreso ninguna de las opciones presentadas.") #Si le erra, o no quiere seguir las normas, entonces le avisamos por pantalla...
    follow=input("¿Desea seguir agregando/buscando contactos?\n\t'SI' para continuar,\n\tCualquier tecla para salir.\n>Respuesta: " )
    follow= follow.upper() #Es importante que follow, siempre vaya en mayusculas. Debido a que si me ingresa 'si', el bucle finalizaria...


    





                






