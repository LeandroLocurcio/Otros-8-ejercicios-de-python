#Ejercicio 5 Guia Propia

numero1=float(input("Introduce el primer numero:"))
numero2=float(input("Introduce el segundo numero:"))

def signo(numero1,numero2):
	contador=0
	if numero1<0:
		contador=contador+1
	if numero2<0:
		contador=contador-1
	if contador==0:
		print("El resultado es positivo")
	else:
		print("El resultado no es positivo")

signo(numero1,numero2)				