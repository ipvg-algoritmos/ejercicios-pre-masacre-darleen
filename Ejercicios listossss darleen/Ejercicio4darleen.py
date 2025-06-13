lista = []

while True:
    numerito = float(input("Ingrese SUS numelitos uwu, para finalizar, escriba un número negativo: "))
    num_uwu= float(numerito)

    if num_uwu < 0:
        break
    lista.append(numerito)
cantidad = len(lista)
print()
promedio = sum(lista) / cantidad

print(f"El promedio de los numeros ingresados es  {promedio} uwu ")