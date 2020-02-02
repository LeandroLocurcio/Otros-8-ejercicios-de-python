#Ejercicio 1 de Guia Propia
Tipo_de_medida=input("Introduce la magnitud de informacion a convertir:")
Cantidad=int(input("Introduce una cantidad de informacion"))
Nueva_magnitud=input("Introduce la nueva magnitud de informacion")
c=0
d=0
x=0
h=0
lista=["Bits","Megabits","Gigabits","Byte","Megabyte","Gigabyte"]
lista2=[1,1000000,1000000000,8,8000000,8000000000]



def conversion(Tipo_de_medida,Cantidad,Nueva_magnitud):
	if Tipo_de_medida in lista and Nueva_magnitud in lista:
		c=lista.index(Tipo_de_medida)
		d=Cantidad*(lista2[c])
		h=lista.index(Nueva_magnitud)
		x=d/(lista2[h])
		print(x)
	
	else:
		print("Magnitud de informacion erronea")
			
conversion(Tipo_de_medida,Cantidad,Nueva_magnitud)
