'''Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad de colillas recolectadas por un
número determinado de personas. Luego obtener estadísticas al respecto informando
porcentaje de personas que han encontrado menos de 100 colillas, más de 100 y menos de 200,
más de 200 colillas. '''

people = int(input("¿Cuantas personas en total recolectaron las colillas de cigarrillos en los barrios?: "))
moreThan200= 0
moreThan100_LessThan200 = 0
lessThan100= 0

for i in range(0, people):
	answerPeople = int(input(f"Persona n°{i+1}:\n ¿Cuantas colillas de cigarrillos recolectaste?: "))
	if answerPeople > 200:
		moreThan200+=1
	elif answerPeople > 100 and answerPeople < 200:
		moreThan100_LessThan200+=1
	else:
		lessThan100+=1

percentLessThan100 = (lessThan100 * 100) / people
percentMoreThan100_LessThan200 = (moreThan100_LessThan200 * 100) / people
percentMoreThan200 = (moreThan200 * 100) / people

print("--------------------Estadisticas---------------")
print(f"-> Las personas que han recolectado menos de 100 colillas: %{percentLessThan100}")
print(f"-> Las personas que han recolectado mas de 100 pero menos de 200: %{percentMoreThan100_LessThan200}")
print(f"-> Las personas que han recolectado mas de 200: %{percentMoreThan200}") 




