'''Diseña un programa al que se proporcione como entradas dos enteros y un carácter.
El programa deberá sumar, restar, multiplicar o dividir los valores de los dos primeros parámetros
dependiendo del código indicado en el tercer parámetro, y devolver el resultado.
Por ejemplo si el usuario ingresa la opción “S”, se deberán sumar los números.'''

def Operator(number, number2, decision):
    decision= decision.upper()
    if decision == 'S':
        print(f"El resultado de la suma es: {number+number2}")
    elif decision == 'R':
        print(f"El resultado de la resta es: {number-number2}")
    elif decision == 'M':
        print(f"El resultado de la multiplicacion es: {number*number2}")
    elif decision == 'D':
        print(f"El resultado de la division es: {number/number2}")
    else:
        print("No eligio ninguna opcion...")

follow = 'SI'
while follow == 'SI':
    number= float(input("Ingrese un numero: "))
    number2=float(input("Ingrese otro numero: "))
    decision=input("¿Que desea realizar?\n1.¿Suma? -> 'S'\n2.¿Resta? -> 'R'\n3.¿Multiplicacion? -> 'M'\n4.¿Division? -> 'D':\nRespuesta: ")
    Operator(number, number2, decision)

    follow = input("¿Desea seguir este programa? Escriba 'si', de lo contrario cualquier tecla...\nRespuesta: ")   
    follow = follow.upper()

