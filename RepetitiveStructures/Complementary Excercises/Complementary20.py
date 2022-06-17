'''El Centro de Salud de Rosario tiene registradas N consultas médicas de menores.
De cada consulta tiene como datos: la edad del menor y el día de visita.
Los datos están ordenados en forma creciente por día.
Proponer un fin de datos para cada día.
Se desea conocer, para cada día, la edad promedio de pacientes y además el día en que se registró el máximo de pacientes.'''
follow= 'SI'
endDay= 'SI'
maxPacient= 0
day = 0
amountPacient= 0 
ageMinor=0
while follow == 'SI':
    endDay= 'SI'
    if amountPacient > maxPacient:
        maxPacient = amountPacient
        dayMaxPacient = day
    while endDay == 'SI':
        day= int(input("Ingrese el dia: "))
        ageMinor+= int(input("Ingrese la edad del menor: "))
        amountPacient+=1
        endDay= input("¿Desea seguir agregando pacientes? 'SI' -> Para seguir, de lo contrario cualquier tecla...\nRespuesta: ")

media = ageMinor / amountPacient
print(f"La edad promedio de pacientes es de: {media} años.")
print(f"El dia en el que se registro la cantidad maxima de pacientes es: {dayMaxPacient}")
