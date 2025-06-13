matriz = [[" ", " ", " "],
           [" ", " ", " "],
            [" ", " ", " "]]

num = int(input("Ingrese su número (1/9)"))
matriz[0][0] = num
num = int(input("Ingrese su número (2/9)"))
matriz[0][1] = num
num = int(input("Ingrese su número (3/9)"))
matriz[0][2] = num
num = int(input("Ingrese su número (4/9)"))
matriz[1][0] = num
num = int(input("Ingrese su número (5/9)"))
matriz[1][1] = num
num = int(input("Ingrese su número (6/9)"))
matriz[1][2] = num
num = int(input("Ingrese su número (7/9)"))
matriz[2][0] = num
num = int(input("Ingrese su número (8/9)"))
matriz[2][1] = num
num = int(input("Ingrese su número (9/9)"))
matriz[2][2] = num

# diagonal principal : (0,0) (1,1) (2,2)
#diagonal secundaria : (0,2) (1,1) (2,0) 
positivo = 0
negativo = 0
cero = 0
diag1 = 0
diag2 = 0
for fila in range(len(matriz)):
  for columna in range(len(matriz[fila])):
    if matriz[fila][columna] > 0:
      positivo += 1
    elif matriz[fila][columna] < 0:
      negativo += 1
    else:
        cero += 1

diag1 = matriz[0][0] + matriz[1][1] + matriz[2][2]
diag2 = matriz[0][2] + matriz[1][1] + matriz [2][0]

if diag1 > diag2:
  print("Diagonal principal es mayor que la diagonal secundaria")
elif diag2 > diag1:
  print("Diagonal secundaria es mayor que la principal")
else:
  print("Ambas diagonales son iguales")

print(f"Suma de diagonal principal es >{diag1}< y la suma de diagonal secundaria >{diag2}<")

print(f"Cantidad de numeros positivos: {positivo}")
print(f"Cantidad de numeros negativos: {negativo}")
print(f"Cantidad de ceros: {cero}")