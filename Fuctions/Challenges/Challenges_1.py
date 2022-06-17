''' 150 años es el tiempo que tarda una bolsa de plástico común en degradarse y
una botella de PET puede tardar 1.000 años en desaparecer. 
Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.
Un trozo de chicle tarda 5 años en degradarse. 
Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.'''

def EvaluationElements(bag=False, bottlePET=False, tetabrik=False, bubbleGum=False):
    if bag != False:
        print("->Una bolsa, tarda un total de 150 años en degradarse.")
    if bottlePET != False:
        print("->Una botella PET puede tardar un total de 1000 años en degradarse.")
    if tetabrik != False:
        print("->Los envases de TETABRIK pueden tardar hasta 30 años en degradarse.")
    if bubbleGum != False:
        print("->Un trozo de chicle tarda 5 años en degradarse.")
    

bag = input("¿Desea agregar una botella para evaluar cuanto años tarda en degradarse?")
if bag == 'SI':
    bag = True
else:
    bag = False
bottlePET = input("¿Desea agregar una botella PET para evaluar cuanto años tarda en degradarse?")
if bottlePET == 'SI':
    bottlePET = True
else:
    bottlePET= False
tetabrik = input("¿Desea agregar una botella para evaluar cuanto años tarda en degradarse?")
if tetabrik.upper()== 'SI':
    tetabrik = True
else:
    tetabrik = False
bubbleGum = input("¿Desea agregar una botella para evaluar cuanto años tarda en degradarse?")
if bubbleGum == 'SI':
    bubbleGum = True
else:
    bubbleGum = False

EvaluationElements(bag, bottlePET, tetabrik, bubbleGum)