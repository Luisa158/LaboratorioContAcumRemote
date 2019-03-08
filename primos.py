
a= int(input("Por favor, ingrese un número "))

contador = 0
for i in range(2,a):
  if a % i == 0:
    contador +=1
    print("divisor:", a)

if contador > 0 :
  print("El número no es primo" )
else:
  print("El número es primo")











