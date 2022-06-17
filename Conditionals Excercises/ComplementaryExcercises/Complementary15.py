'''Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:

i. Si trabaja 40 horas o menos se le paga $16 por hora

ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.'''

hours = int(input("Ingrese la cantidad de horas trabajadas semanalmente: "))
if hours <= 40:
	weeklySalary= hours*16
else: 
	weeklySalary= (40*16) + ((hours-40)*20)

print(f"->Su salario semanal es de: ${weeklySalary}")