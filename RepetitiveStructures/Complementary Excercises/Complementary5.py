'''5) Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar.
El ciclo debe finalizar cuando el usuario ingresa 0 '''

follow= 0
while follow == 0:
    number= int(input("Ingrese por favor un numero: "))
    if number % 2 == 0:
        print(f"El numero {number} es PAR.")
    else:
        print(f"El numero {number} es IMPAR.")
    follow=(int(input("Si desea comprobar con otro numero, presione el numero 0, de lo contrario cualquier tecla...\nDecision: ")))

    
