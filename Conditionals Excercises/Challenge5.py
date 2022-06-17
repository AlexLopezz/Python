'''La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la barrio y
el tipo del barrio (CÉNTRICO y NO CÉNTRICO)
*La sección A esta formada por los barrios céntricos cuyo nombre comienza con una letra anterior a M y los
barrios no céntricos con nombre posterior a la M, y la sección B el resto.

-> Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra'''

neighborhood = input("Indique por favor el nombre del barrio: ")
locate = input("Ingrese por favor la tecla C si su barrio es Centrico o la tecla NC si su barrio No es Centrico: ")

if locate == "C" and neighborhood.lower() < "m": #Si es centrico... y Si la primer letra es anterior a la m, entonces...
		print(f"Su barrio: {neighborhood}, que es de una zona centrica({locate}). Pertenece a la SECCION A.")
elif locate == "NC" and neighborhood.lower() > "m": #Si es centrico...  y si la primer letra es posterior a la m, entonces... 
		print(f"Su barrio: {neighborhood}, que es de zona NO Centrica. Pertenece a la SECCION A.")
else: 
	if locate == "C":
		print(f"Su barrio: {neighborhood}, que es de una zona centrica({locate}). Pertenece a la SECCION B.")
	elif locate == "NC":
		print(f"Su barrio: {neighborhood}, que es de una zona NO centrica({locate}). Pertenece a la SECCION B.")


