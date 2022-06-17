'''Un grupo de 100 estudiantes presentan un exámen de Física.
Diseñe un diagrama que lea por cada estudiante la calificación obtenida y calcule e imprima:
A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.
B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 80.
C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.
D. La cantidad de estudiantes que obtuvieron una calificación de 80 o más. '''
amountStudents=0
LessThanFifty=0
greaterThanFiftyMinorEighty=0
greaterThanSeventyMinorEighty=0
greaterThanEighty=0

for estudiante in range(0,10):
    amountStudents+=1
    print(f"Estudiante N°{estudiante+1}")
    studentNote= float(input("Ingrese por favor la nota correspondiente del estudiante: "))
    if studentNote > 80:
        greaterThanEighty+=1
    elif studentNote >= 70 and studentNote < 80:
        greaterThanSeventyMinorEighty+=1
    elif studentNote >= 50 and studentNote < 80:
        greaterThanFiftyMinorEighty+=1
    else:
        LessThanFifty+=1
    
print("----------RESULTADOS---------")
print(f"Cantidad de estudiantes encuestados: {amountStudents}")
print(f"Cantidad de alumnos con nota menor a 50: {LessThanFifty}")
print(f"Cantidad de alumnos con notas de 50 o más pero menor que 80: {greaterThanFiftyMinorEighty}")
print(f"Cantidad de alumnos con notas de 70 o más pero menor que 80: {greaterThanSeventyMinorEighty}")
print(f"Cantidad de alumnos con notas mayor a 80: {greaterThanEighty}")