print("Uso del break: Se utiliza en bucles while, for y sirve simplemente para terminar el bucle donde se lo invoca.")

names = ["alex", "daniel", "agustin", "galo"]

for i in range(len(names)):
	print(names[i])
	if names[i] == "daniel":
		print(f"Se encontro a la persona: {names[i]}.\nSe saldra del bucle.\n")
		break

print("\nUso del continue: Regresa al comienzo del bucle e inicia la siguiente iteraccion.")
for i in "python":
	if i == "h":
		continue
	print(i)

print("\nUso del pass: No realiza ninguna accion, se utiliza cuando se requiere una declaracion"
	+"\npero no se requiere ejecutar ningun comando o codigo.")

for i in "python":
	if i == "h":
		pass
	print(i)

#A diferencia con continue, pass si imprime la letra o lo que esta despues de ella.


