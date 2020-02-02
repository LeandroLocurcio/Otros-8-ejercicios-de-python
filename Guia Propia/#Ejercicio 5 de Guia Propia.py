#Ejercicio 7 de Guia Propia

hora1=int(input("Introduce la primera hora:"))
hora2=int(input("Intrduce la segunda hora:"))

def segundos(hora1,hora2):
	segundos=0
	if 0<hora1<24 and 0<hora2<24:
			if hora1>hora2:
				segundos=(24+hora2-hora1)*(60**2)
				print(segundos)
			else:
				segundos=(hora2-hora1)*(60**2)
				print(segundos)

	else:
		print("La hora introducida es incorrecta")				
	

segundos(hora1,hora2)		