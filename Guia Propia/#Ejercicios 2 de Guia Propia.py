#Ejercicios 3 de Guia Propia

segundos = int(input("Introduce una cantidad de segundos:"))
minutos = int(input("Introduce una cantidad de minutos:"))
horas = int(input("Introduce una cantidad de horas:"))

def segundostotales(segundos,minutos,horas):
	minutosr=0
	horasr=0
	x=0
	minutosr=minutos*60
	horasr=horas*(60**2)
	x=segundos + minutosr + horasr
	print(x)

segundostotales(segundos,minutos,horas)	