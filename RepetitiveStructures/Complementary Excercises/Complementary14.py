'''Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes.
Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras
tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule
el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras.
El precio de venta será 1.5 veces el costo total, que viene determinado por el tamaño,
más el número de ingredientes. En particular el costo total se calcula sumando:

- un costo fijo de preparación.

- un costo variable que es proporcional al tamaño de la pizza.

- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada ingrediente extra tiene el mismo costo).'''

#Abstraccion: 
#Tres tamaños: pequeña, mediana y grande. 
#Costo fijo de preparacion.
#Costo adicional por ingredientes extras...
#o con ingredientes extras tales como pepinillos, champiñones o cebollas.

FIXED_COST= 200 #Costo fijo de preparacion
follow= "SI"
SMALL = 150
MEDIUM = 200
BIG = 250

totalPricePizza=0

while follow == "SI":
    print("----------PREPARACION DE PIZZA--------")
    decision= input("¿Que tamaño de pizza quiere?\n1. Pequeña\n 2. Mediana\n 3. Grande\nDecision: ")
    if decision == '1':
        totalPricePizza+= SMALL
    elif decision == '2':
        totalPricePizza+= MEDIUM
    elif decision == '3':
        totalPricePizza+= BIG
    else:
        continue

    typeOfPizza = input("¿Que tipo de pizza quiere?\n1.Sencilla\n2.Con Ingredientes extras.")
    if typeOfPizza == '1':
        totalPricePizza+= 100 #Si es sencilla, le sumamos 100 nomas.
    elif typeOfPizza == '2':
        typeOfPizza = input("¿Desea agregar pepinillos?. Escriba 'si', de lo contrario cualquier tecla: ")
        if typeOfPizza.lower() == 'si':
            totalPricePizza+= 50
        typeOfPizza = input("¿Desea agregar champiñones?. Escriba 'si', de lo contrario cualquier tecla: ")
        if typeOfPizza.lower() == 'si':
            totalPricePizza+= 50
        typeOfPizza = input("¿Desea agregar cebollas?. Escriba 'si', de lo contrario cualquier tecla: ")
        if typeOfPizza.lower() == 'si':
            totalPricePizza+= 50
    
    totalPricePizza+= FIXED_COST
    totalPricePizza*= 1.5
    print(f"->El precio de la pizza es de: ${totalPricePizza}")

    follow= input("¿Desea calcular el precio de otra pizza?Escriba 'si' de lo contrario cualquier tecla...\nRespuesta: ")
    follow= follow.upper()


