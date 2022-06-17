''' Los alumnos de un curso se han divido en dos grupos A y B de acuerdo
al sexo y el nombre
El grupo A esta formado por las mujeres con un nombre anterior a la M y los
hombres con un nombre posterior a la N.
El grupo B por el resto. Escribir un programa que pregunte al usuario su nombre
y sexo. Muestre por pantalla el grupo que le corresponde.'''

name = input("Por favor ingrese su nombre: ")
sexOfPerson = input("Bien, ahora ingrese por favor su genero(F o M): ")

if sexOfPerson == "F":
	if name.lower() < "m":
		print(f"Su nombre: {name}.\nGenero: {sexOfPerson}.\nGrupo al que corresponde: A.")
elif sexOfPerson == "M":
	if name.lower() > "n":
		print(f"Su nombre: {name}.\nGenero: {sexOfPerson}.\nGrupo al que corresponde: A.")
else:
	print(f"Su nombre: {name}.\nGenero: {sexOfPerson}.\nGrupo al que corresponde: B.")