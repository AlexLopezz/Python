'''Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B. 
El programa no permitirá introducir valores negativos para A y B y verificará que A es menor que B.
 Si A es mayor que B, se deben intercambiar los valores.'''

A= -1
B= -1
while A < 0:
    A = int(input("Ingrese un valor para A: "))
    B = int(input("Ingrese un valor para B: "))
    if A < 0 or B < 0:
        print("Por favor, debe ingresar valores numericos naturales. De otra forma no podremos seguir con este programa.")


addMultipleFive=0
if A > B:
    aux = A
    B = A
    A = aux
    for i in range(A,B):
        if i % 5 == 0:
            print(i)
            addMultipleFive+=i
    
    print(f"La suma de los numeros multiplos de 5 que hay entre {A} y {B} es de {addMultipleFive}")
else:
    for i in range(A,B):
        if i % 5 == 0:
            print(i)
            addMultipleFive+=i
    
    print(f"La suma de los numeros multiplos de 5 que hay entre {A} y {B} es de {addMultipleFive}")




 