#Ejercicio 8 de Guia Propia

dia=int(input("Introduce el dia:"))
mes=int(input("Introduce el mes:"))
anio=int(input("Introduce el año:"))

contador=0

def paso_previo(anio):
	global contador
	if anio%4==0:
		contador=contador+1
	if anio%100==0:
		contador=contador+1

	if anio%400==0:
		contador=contador+1

	if contador==0 or contador==2:
		print("El año no es bisiesto")	
	else:
		print("El año es bisiesto")

paso_previo(anio)			

lista3=[31,59,90,120,151,181,212,243,273,304,334,365]
lista4=[31,60,91,121,152,182,213,244,274,305,335,336]


if contador==0 or contador==2:
	for i in lista3:
		if mes==lista3.index(i)+1:
			resultado=lista3(i)+dia
else:
	for i in lista4:
		if mes==lista4.index(i)+1:
			resultado=lista4(i)+dia
print(resultado)			

