#Create my class Time:
class Time:
    def __init__(self):
        self.__hour = 00
        self.__minutes = 00
        self.__seconds = 00
    
    #Metodos getters:
    def getHour(self):
        return self.__hour
    def getMinutes(self):
        return self.__minutes
    #Metodos setters:
    def setHour(self, newHour):
        if(newHour >=0 and newHour < 24):
            self.__hour = newHour
        else:
            print(f"No se puede modificar el horario, debido a que no existe el horario {newHour}")

    def addHour(self, minutes):
        hours = minutes // 60 #Calculo la hora
        min = hours * 60
        self.__minutes+= min #Calculo los minutos
        self.__hour+= hours



    def setMinutes(self, newMinutes):
        if(newMinutes >= 0 and newMinutes < 60): #1 hora son 60 minutos
            self.__minutes = newMinutes 
        elif(newMinutes >= 0 and newMinutes >= 60): #Si pasan los 60 minutos, significa que es una hora:
            self.addHour(newMinutes)

        else:
            print(f"No se puede modificar los minutos, debido a que no existe el minuto {newMinutes}")
    
    def __str__(self):
        return f"Son las {self.getHour()} y {self.getMinutes()} hs."
        
class Prueba_Tiempo:
    def __init__(self, tiempo):
        self.__time = tiempo

    def modifyHour(self, newHour):
        self.__time.setHour(newHour)
    def modifyMinutes(self, newMinutes):
        self.__time.setMinutes(newMinutes)

    def showTime(self):
        print(self.__time)
    
tiempo = Time()
pruebaHora = Prueba_Tiempo(tiempo)
pruebaHora.modifyHour(21)
pruebaHora.modifyMinutes(65)
pruebaHora.showTime()
