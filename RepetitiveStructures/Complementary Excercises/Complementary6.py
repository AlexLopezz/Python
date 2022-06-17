#Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, tal que el segundo sea mayor o igual que el primero.


i = 0
addMultiple=0
count=0
until = int(input("Por favor ingrese un numero: "))
#Con FOR.
print("CON FOR")
for it in range(i,until,2):
        print(it)
        addMultiple+= it
        count+=1

print(f"La cantidad total de numeros multiplos de 2 entre {i} y {until} es {count}")
print(f"La suma total de los numeros multiplos de 2 es de {addMultiple}")

'''Con WHILE
print("CON WHILE")
while i < until:
    if i%2==0:
        count+=1
        addMultiple+=i
        i+=1


print(f"La cantidad total de numeros multiplos de 2 entre {i} y {until} es {count}")
print(f"La suma total de los numeros multiplos de 2 es de {addMultiple}") '''