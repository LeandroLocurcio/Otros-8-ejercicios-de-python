#Ejercicio con Nico
#Imprimir en pantalla los elementos de una lista en orden inverso

lista=[5,8,9,4,2,5,4,6]

def funcion(lista):
	lista2=[]
	for i in lista:
		lista2.append(0)
	c=len(lista)
	t=0
	for i in lista:
		t=t+1
		lista2.insert(c-t,i)
		lista2.pop(c-t+1)
	return lista2

h=funcion(lista)
print(h)
		
		





		








