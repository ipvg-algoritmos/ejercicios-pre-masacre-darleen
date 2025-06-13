ingresar_texto = input("Escibre una cadena de texto: ")
consonante = 0
vocal = 0

for letra in ingresar_texto:
    if  letra in "aeiou":
        vocal = vocal+1
    elif letra in "áéíóúbcdfghjklmnñpqrstvwxyz":
        consonante = consonante+1

print(f"Hay un total de: {vocal} vocales y {consonante} consonantes")