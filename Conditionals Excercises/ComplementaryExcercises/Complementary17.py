'''Determinar y exhibir si la estatura de una persona adulta dada, es mayor que la estatura media
de las personas adultas de su sexo, siendo:

- estatura media de mujeres adultas: 1,65 m.

- estatura media de varones adultos: 1,72 m. '''

sexOfPerson = input("Necesito que digite su sexo, si es femenino, presione 'f' . Si es masculino, presione'm'\nRespuesta: ")
if sexOfPerson == "f":
	heigthPerson = float(input("Ingrese su altura: "))
	if heigthPerson > 1.65:
		print(f"La altura de usted({heigthPerson}m) es MAYOR a la media de estaturas de su sexo.(1.65m)")
	else:
		print(f"La altura de usted({heigthPerson}m) no es MAYOR a la media de estaturas de su sexo.(1.65m)")
elif sexOfPerson == "m":
	heigthPerson = float(input("Ingrese su altura: "))
	if heigthPerson > 1.72:
		print(f"La altura de usted({heigthPerson}m) es MAYOR a la media de estaturas de su sexo.(1.65m)")
	else:
		print(f"La altura de usted({heigthPerson}m) no es MAYOR a la media de estaturas de su sexo.(1.65m)")
else:
	print("Usted no ingreso su sexo...")

