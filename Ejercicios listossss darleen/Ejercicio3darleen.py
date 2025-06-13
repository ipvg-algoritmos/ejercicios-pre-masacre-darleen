lista = []

while True:
    numerito = int(input("Ingrese SUS numeros y ingrese un número negativo para finalizar: "))
    num_uwu= float(numerito)

    if num_uwu < 0:
        break
    lista.append(numerito)

if lista:
    mayor_owo = lista[0]
    menor_unu = lista[0]
    for numero in lista:
        if numero > mayor_owo:
            mayor_owo = numero
        if numero < menor_unu:
            menor_unu = numero

print(f"La lista ingresada es : {lista}")
print(f"El numerito mayor de la listita es : {mayor_owo}")
print(f"El numerito menor de la listita es : {menor_unu}")