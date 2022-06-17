#4) Diseñar un programa que imprima los números del 100 al 0 en orden decreciente.

print("Con for: ")
for numero in range(100,-1,-1): #De 100 a -1, con saltos de -1, es decir que para que me cuente le 0, debo ingresar un numero antes del 0(-1)
    print(numero)

print("Con while: ")
numero=100
while numero >= 0:
    print(numero)
    numero-=1
    