# Programa-para-determinar-si-un-a-o-es-bisiesto-o-no
#El siguiente programa sirve para determinar si un año es o fue bisiesto o no

anyo=int(input("Introduzca el año:"))

if isinstance(anyo/4,int):
	print("El año es bisiesto")

elif isinstance(anyo/4,int) and isinstance(anyo/100,int) and isinstance(anyo/400,float):
	print("El año no es bisiesto")	

elif isinstance(anyo/4,int) and isinstance(anyo/100,int) and isinstance(anyo/400,int):
	print("El año es bisiesto")

else:
	print("El año no es bisiesto")	

if isinstance(400/400,int):	
	print(x)


