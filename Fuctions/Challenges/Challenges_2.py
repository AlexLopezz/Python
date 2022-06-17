''' Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de
dos ciudades se cumpla lo siguiente:
>Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
>Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
>Si ambos números son iguales, debe devolver el nombre de ambas. '''

def relation(a=1,b=1):
        if a and b != 1:
            if a > b:
                return 1
            elif a < b:
                return 2
            else:
                return 3
    

city = input("Ingrese el nombre de la ciudad: ")
amountTonsCity = int(input(f"Ingrese la cantidad de toneladas recicladas de la ciudad {city}:"))
city2 = input("Ingrese el nombre de la ciudad: ")
amountTonsCity2 = int(input(f"Ingrese la cantidad de toneladas recicladas de la ciudad {city2}:"))
resultRelation= relation(amountTonsCity,amountTonsCity2)
if resultRelation == 1:
    print(f"->La ciudad {city} reciclo un total de {amountTonsCity}.")
elif resultRelation == 2:
    print(f"La ciudad {city2} reciclo un total de {amountTonsCity2}")
else:
    print(f"->La ciudad {city} y {city2} reciclaron la misma cantidad de basura reciclada. Toneladas recicladas: {amountTonsCity}.")


