'''Ejercicio2.
En una jurisdicción particular, las tarifas de taxi consisten en una tarifa base de $40.00, más $15.00 por cada 140 metros recorridos.
Escriba una función que tome la distancia recorrida (en kilómetros) como su único parámetro y devuelva la tarifa total como su único resultado.
Escriba un programa principal que use la función.'''

def tarifa(kmTraveled):
    FIXED_COST= 15
    BASE_RATE= 40
    RateTotal= ((kmTraveled//140)* FIXED_COST) + BASE_RATE
    return RateTotal

kmTraveled = float(input("Ingrese por favor los kilometros recorridos: "))
print(f"La tarifa total a pagar es de: ${tarifa(kmTraveled)}")

    

