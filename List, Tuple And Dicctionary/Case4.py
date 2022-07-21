''' Realice una función que dada una lista de enteros L, y un número entero n.
Elimine de la lista original los elementos que sean iguales a ese número dado.'''

import random

def fillList(aList,n):
    for i in range(0,n):
        aList.append(random.randint(1,100))
    return aList

def checkListNumber(aList, number):
    for e in aList:
        if e == number:
            print(f"Se borro el elemento {e}")
            aList.remove(e) 
    print(aList)
listNull = [64]
listNull = fillList(listNull, 10)

checkListNumber(listNull, 64)
