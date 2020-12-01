'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna
C) O maior valor da segunda linha
'''

cols = []
soma = 0
som_col = 0
maior = 0
pares = []
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
            soma = sum(pares)
        if matriz[l][2]:
            cols.append(matriz[l][2])
            som_col = sum(cols)

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos números pares é {soma}')
print(f'A soma dos valores da terceira coluna é {som_col}')
print(f'O maior valor da segunda linha é {maior}')