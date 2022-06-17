'''Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el primer elemento y $ 2.95 para cada segundo elemento posterior.
Escriba una función que tome el número de elementos en el pedido como su único parámetro.
Devuelva los gastos de envío del pedido como resultado de la función.
Incluya un programa principal que lea la cantidad de artículos comprados al usuario y muestre los gastos de envío. '''

def CostoEnvio(numberElements):
    totalCostDelivery = 0
    firstElement = 10.95
    GeneralElements = 2.95
    if numberElements > 1:
        totalCostDelivery = ((numberElements-1)*GeneralElements) + firstElement
        return totalCostDelivery
    else:
        return firstElement 

numberElements = int(input("Ingrese por favor la cantidad de elementos que va a enviar: "))
print(f"Los gastos de envio del pedido es: ${CostoEnvio(numberElements)}")


