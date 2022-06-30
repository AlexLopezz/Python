def suma(a,b):
  resul = a+b
  return resul
def resta(a,b):
  resul = a-b
  return resul
def multiplicacion(a,b):
  resul = a*b
  return resul
def division(a,b):
    if b!= 0:
        resul = a/b
        return resul
    else:
        return 0


print("Bienvenidos a mi calculadora :)\n")
m= "SI"
while m == "SI":
    x = float(input(f"INGRESE SU PRIMER NUMERO:\t"))
    y = float(input(f"INGRESE SU SEGUNDO NUMERO:\t"))
    print("Que queres hacer?")
    decision = input(f"1= suma\n" "2= resta\n" "3= multiplicacion\n"  "4= division\n")
    if decision=="1":
        print(f"El resultado es {suma(x,y)}")
    elif decision=="2":
        print(f"El resultado es {resta(x,y)}")
    elif decision=="3":
        print(f"El resultado es {multiplicacion(x,y)}")
    elif decision=="4":
        if division(x,y)!=0:
            print(f"El resultado es {division(x,y)}")
        else:
            print ("No se puede realizar esta division")
    m=input("¿Desea seguir con la operacion?\nSI -> 'SI'\n NO -> cualquier tecla\nRespuesta: ")
    m= m.upper()
