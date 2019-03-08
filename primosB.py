
a= int(input("Por favor, ingrese un número "))

i = 1
cont=0

while i<=a:

    if a % i == 0:
        print("divisor:", i)
        cont=cont+1


    i=i+1

if cont> 2:
 print("El número no es primo")
else:
     print("El número es primo")


