#Prueba de años bisiestos en lista

import math

dia=int(input("Introducir el dia de la fecha:"))
mes=int(input("Introducir el mes de la fecha:"))
anio=int(input("Introducir el año de la fecha:"))
dias_a_sumar=int(input("Introduce una cantidad de dias a sumar:"))	
	
contador=0	

if anio%4==0:
	contador=contador+1

if anio%100==0:
	contador=contador+1


if anio%400==0:
	contador=contador+1


o=0
if mes==1 or (mes==2 and dia<=28):
	o=1

c=math.floor(dias_a_sumar/365)#Es igual a la cantidad de años que pasaron si todos fueran no bisiestos

f=dias_a_sumar%365#Es la parte nominal de la cantidad de dias

k=list(range(anio+1,anio+c+1))

print(dia)
print(f)
print(k)

contador2=0

#print(o)

l=0	

for i in k:#Con este programa quiero ver en una range que cantidad de años son bisiestos y cuales no
	#print(i)
	if contador2!=0:
		contador2=0

	if i%4==0:
		contador2=contador2+1

	if i%100==0:
		contador2=contador2+1

	if i%400==0:
		contador2=contador2+1

	if contador2==0 or contador2==2:
		l=l+1	#l es la cantidad de años no bisiestos en ese intervalo
	else:
		o=o+1   #o es la cantidad de años bisiestos en ese intervalo

lista=(31,28,31,30,31,30,31,31,30,31,30,31)
lista2=(31,59,90,120,151,181,212,243,273,304,334,365)
lista3=(31,60,91,121,152,182,213,244,274,305,335,336)


z=0#Esto sera la cantidad de dias nominales despues de que le sume
#la cantidad de dias


contador0=0

if contador==0 or contador==2:
	for i in lista2:
		contador0=contador0+1
		if mes==contador0:
			z=lista2[mes-1]
			break
		
else:
	for i in lista3:
		contador0=contador0+1
		if mes==contador0:
			z=lista3[mes-1]
			break

print(z)

h=z+dia+f-o	

print(h)







