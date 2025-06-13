lista = [1,2,3,4,5,6,7,8,9,10]

numero = int(input("ingrese un numero de la lista: "))

for i in range(len(lista)):
  if numero == lista[i]:
    print(f"el numero {numero} está dentro de la lista en la posición {i}")
    break
  if i + 1 == len(lista):
    print("El numero ingresado no está en la lista")