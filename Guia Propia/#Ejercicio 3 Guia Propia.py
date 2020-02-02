#Ejercicio 4 Guia Propia

segundos = int(input("Introduce una cantidad de segundos:"))

def equivalente(segundos):
	minutos= 0
	horas= 0
	dias= 0
	semanas= 0
	meses= 0
	minutos= segundos/60
	horas= minutos/60
	dias= horas/24
	semanas= dias/7
	meses= dias/30
	print("La cantidad de minutos equivalentes es"+ str(minutos))
	print("La cantidad de horas equivalentes es"+ str(horas))
	print("La cantidad de dias equivalentes es"+ str(dias))
	print("La cantidad de semanas equivalentes es"+ str(semanas))
	print("La cantidad de meses equivalentes es"+ str(meses))

	
equivalente(segundos)