#Ejercicio 8 de Guia Propia

dia=int(input("Introduce el dia:"))
mes=int(input("Introduce el mes:"))
anio=int(input("Introduce el año:"))

dia_actual=int(input("Introduce el dia actual:"))
mes_actual=int(input("Introduce el mes actual:"))
anio_actual=int(input("Introduce el año actual:"))

c=anio_actual-anio-1

if mes_actual>mes:
	c=c+1
if mes_actual==mes and dia_actual>=dia:
	c=c+1

print(c)		

