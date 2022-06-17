
'''Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.

Ingredientes comunes: Verduras y berenjena.

Ingredientes Receta 1: Lentejas y apio.

Ingredientes Receta 2: Morrón y Cebolla..

Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta le muestre un menú
 con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente (entre la receta elegida y los comunes.)
  y el tipo de receta. Al final se debe mostrar por pantalla la receta elegida y todos los ingredientes. '''

print("RECETAS ECOLOGICAS:\nReceta 1.\nReceta 2.")
recipe = input("¿Que tipo de receta desea? (r1 o r2): ")

if recipe == "r1":
	print("Elija 3 ingredientes: ")
	print("1. Verduras\n2. Berenjena\n3. Lentejas\n4. Apio")
	ingredient1 = input("Ingrediente n°1: ")
	ingredient2 = input("Ingrediente n°2: ")
	ingredient3 = input("Ingrediente n°3: ")
	print(f"Receta elegida: r1\nIngredientes:\n{ingredient1}\n{ingredient2}\n{ingredient3}")
elif recipe == "r2":
	print("Elija 3 ingredientes: ")
	print("1. Verduras\n2. Berenjena\n3. Morron\n4. Cebolla")
	ingredient1 = int(input("Ingrediente n°1: "))
	ingredient2 = int(input("Ingrediente n°2: "))
	ingredient3 = int(input("Ingrediente n°3: "))

print(f"Receta elegida: r2\nIngredientes:\n{ingredient1}\n{ingredient2}\n{ingredient3}")
