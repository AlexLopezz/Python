'''Determinar si un alumno aprueba o reprueba un curso sabiendo que aprobara
si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario.'''

note1 = float(input("NOTA N°1: "))
note2 = float(input("NOTA N°2: "))
note3 = float(input("NOTA N°3: "))

promedio= (note1+note2+note3) / 3

if promedio >= 70:
	print(f"->El alumno esta en condiciones de APROBAR el curso.\n[?]Promedio: {promedio}")
else:
	print(f"->El alumno esta en condiciones de DESAPROBAR el curso.\n[?]Promedio: {promedio}")
