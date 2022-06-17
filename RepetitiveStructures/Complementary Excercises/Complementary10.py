#10) Mostrar los perímetros de varios triángulos ingresados sus lados por teclado, hasta que ya no desee.

follow= "SI"

while follow== "SI":
    base= float(input("Ingrese la base de su triangulo: "))
    sideA= float(input("Ingrese el lado A de su triangulo: "))
    sideB= float(input("Ingrese el lado B de su triangulo: "))
    if base==sideA and base==sideB:
        perimeter= 3 * base
        print("Tipo de triangulo: Equilatero.")
    elif sideA == sideB and sideA != base:
        perimeter= 2* sideA + base
        print("Tipo de triangulo: Isosceles.")
    else:
        print("Tipo de triangulo: Escaleno.")
        perimeter= sideA + sideB + base
    print(f"El perimetro es de {perimeter}")
    follow=input("Si desea seguir calculando el perimetro de un triangulo, escriba 'SI'.\nDecision: ")
    follow= follow.upper()


