''' Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles
plantados en diferentes ciudades de Argentina durante la cuarentena.
Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100
y la segunda con el resto.
Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.'''

def separar(lista):
    count = 0
    countCityThan100=0
    countCityMinorThan100 = 0
    cityThan100 = []
    cityMinorThan100 = []
    for it in lista:
        if it > 100:
            cityThan100.append(it)
            count+=1
        else:
            cityMinorThan100.append(it)
    
    print(f"La cantidad de ciudades que plantaron MAS de 100 arboles durante la cuarentena es de {count}.")

    decision= input("¿Quiere ver la cantidad reciclada por cada ciudad?\n\t'SI' -> si lo desea.\n\tCualquier tecla de lo contrario\nDecision: ")
    if decision.upper() == 'SI':
        cityThan100.sort()
        print("Ciudades que plantaron MAS de 100 arboles: ")
        for it in cityThan100:
            countCityThan100+=1
            print(f"Ciudad N°{countCityThan100}: {it}")
        
        cityMinorThan100.sort()
        print("Ciudades que plantaron MENOS de 100 arboles: ")
        for it in cityMinorThan100:
            countCityMinorThan100+=1
            print(f"Ciudad N°{countCityThan100}: {it}")
    else:
        print("Este programa finalizo...")

TreeCity = [234,12123,3443,2323,443,33,21,45,23,1112,4341,222,2222234]
separar(TreeCity)



        