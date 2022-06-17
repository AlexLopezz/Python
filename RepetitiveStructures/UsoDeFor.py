'''x = 0
while x <= 10:
	print(x)
	x+=1

print(x) '''

'''Programa que genera una multiplicacion de dos numeros del 2 al 10 al azar.
Pregunte por el resultado y diga si se ha dado la respuesta correcta. Al inicio
debe preguntar cuantas multiplicaciones se van hacer.

El programa debe llevar la cuenta de las respuestas correctas e incorrectas. Indicar
la nota correspondiente.
	Si la nota es igual o mayor que 9, el programa felicitara al usuario por el resultado
	Si se acieta la respuesta, se contabiliza como 1
	Si se acerca menos del 10% a la respuesta correcta, se contabiliza como 0.65
	Si se acerca entre el 10% y el 30% a la respuesta correcta, se contabiliza como 0.33
	Si se aleja mas del 30% de la respuesta correcta, se contabiliza como 0.
'''
#Importamos una libreria
from random import randrange
correctAnswer = 0

amount = int(input("¿Cuantas multiplicaciones se realizaran?"))
i = 0
for i in range(0, amount):
	multiplier = randrange(2,10)
	multiplying = randrange(2,10)
	totalMultiply = multiplier * multiplying
	answer = int(input(f"Ingrese la respuesta que cree que es correcta de la multiplicacion entre {multiplier} * {multiplying}: "))
	detour= (abs(totalMultiply - answer)/totalMultiply)/100

	if detour == 0:
		correctAnswer+=1
	elif detour <= 10:
		correctAnswer+= 0.65
	elif detour >=10 and detour <= 30:
		correctAnswer+= 0.33
	elif detour > 30:
		correctAnswer = 0

note = (correctAnswer/amount)*100

if note >= 9:
	print("Felicitaciones, usted logro la nota mas alta.")
	print(f"Su nota final es: {note}")
else:
	print(f"Su nota final es: {note}")


