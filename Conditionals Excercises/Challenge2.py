'''La contaminación del agua se detecta en los laboratorios,  donde pequeñas muestras de agua se analizan
para diversos tipos de contaminantes. Los organismos vivos tales como pescados se pueden también utilizar
para la detección de la contaminación del agua. Los cambios en su comportamiento o crecimiento nos
demuestran,  que el agua en la que viven está contaminada.

Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python
que dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:

Tamaño Normal: Mensaje "Pez en buenas condiciones"
Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"
Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"
Tamaño sobredimensionado: Mensaje "Pez contaminado"'''

lengthFish= float(input("Ingrese por favor el tamaño del pez(en cm): "))

if lengthFish > 17.8:
	print("El tamaño del pez, indica que esta conminado.") 
elif lengthFish > 17.5 and lengthFish <= 17.8:
	print("El tamaño del pescado, indica que tiene sintomas de organismo contaminado")
elif lengthFish > 17 and lengthFish <= 17.5:
	print("El tamaño del pescado esta en buenas condiciones.")
else: 
	print("El tamaño del pez, indica ue tiene problemas de nutricion.")

#Como la consigna no me dio parametros de cuanto media un pez, me base en la siguiente informacion: https://www.guiarecursospesqueros.org/peces-oseos/
