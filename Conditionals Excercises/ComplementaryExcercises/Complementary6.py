'''Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un
aumento del salario para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma:
Sueldo Actual (en $)    Aumento

0 – 6000				15%

6000 – 7900			    10%

7900 – 12000			6%

Más de 12000			0%
Diseñar un programa que lea el salario de un jugador, y que a continuación muestre el tanto por
ciento de aumento, el sueldo actual y el sueldo aumentado. '''

salary = float(input("Ingrese por favor su salario: "))
if salary > 0:
	if salary > 12000:
		print(f"Usted cobra mas de $12000(${salary}), por lo que no hay aumentos para usted.")
	elif salary >= 7900 and salary <= 12000:
		salary*= 1.06
		print(f"->Su aumento es del 6% por lo que su nuevo saldo es de ${salary}")
	elif salary > 6000 and salary <= 7900:
		salary*= 1.10
		print(f"->Su aumento es del 10% por lo que su nuevo saldo es de ${salary}")
	else: 
		salary*=1.15
		print(f"->Su aumento es del 15% por lo que su nuevo saldo es de ${salary}")
else:
	print("[X]Usted debe ingresar un salario mayor a 0, para saber el aumento de su salario actual.")