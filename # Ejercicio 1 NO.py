#Cualificacion-de-triangulos-segun-sus-lados
#El objetivo de este programa es cualificar de que tipo de triangulo  (Isoceles , Escaleno , Equilatero) tomando como input sus lados
#Los lados de un triagnulo los definiremos como A,B y C

A=int(input("Introduce el lado A el triangulo:"))

B=int(input("Introduce el lado B el triangulo:"))

C=int(input("Introduce el lado C el triangulo:"))

i=1
#Para que este mas piola lo que sigue deberia estar con mayor o igual , pero no lo encontre en mi teclado XD
if A+B>C:
	i=i+1

if A+C>B:
	i=i+1

if C+B>A:
	i=i+1

if i==4:
   print("Es un triangulo")
else:
  print("No es un triangulo") 


if A==B:
	i=i+20

if A==C:
	i=i+20

if C==B:#Creo que esta condicion esta de mas
    i=i+20

if i==64:
   print("No solo es un triangulo sino que tambien es Equilatero")

if i==24:
   print("No solo es un triangulo sino que tambien es isoceles")

if i==4:
   print("No solo es un triangulo sino que tambien es escaleno")          

    









