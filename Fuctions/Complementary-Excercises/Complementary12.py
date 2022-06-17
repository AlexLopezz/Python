'''
Ejercicio 12: Próximo Siguiente
En este ejercicio creará una función llamada proximo_primo que encuentra y devuelve el primer número primo mayor
que algún número entero, n.
El valor de n se pasará a la función como su único parámetro. 
Incluya un programa principal que lea un número entero del usuario y muestre el primer número primo mayor que el
valor ingresado. '''

def Es_Primo(entero):
    for i in range(2,entero):
        if entero % i == 0:
            return False
    return True

def proximo_primo(entero):
    i= (entero+1)
    while not Es_Primo(i):
        i+=1
    return i
    
entero= int(input("Ingrese por favor un numero: "))
print(f">El proximo numero primo mas cercano del numero {entero} es el {proximo_primo(entero)}.")    
print(proximo_primo(23))