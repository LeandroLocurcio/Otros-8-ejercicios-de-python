#De verdad P para deter año bisiesto.

anio=int(input("Introduzca el año:"))


contador=0		

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





