"""
Desafio 087: Aprimore o desafio
anterior, mostrando
no final:

A) A soma de todos os
valores pares
digitados.

B) A soma dos valores
de terceira coluna.

C) O maior valor da
segunda linha.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior2 = 0
p = 0
soma3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l},{c}: '))
        if matriz[l][c] % 2 == 0:
            p += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
print('='*50)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('='*50)
maior2 = max(matriz[1])
print(f'A soma dos números pares digitados é {p}')
print(f'A soma dos valores da terceira coluna é {soma3}')
print(f'O maior valor da segunda linha é {maior2}')