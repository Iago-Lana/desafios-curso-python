"""
Desafio 086: Crie um programa
que crie uma matriz de
dimensão 3x3 e
preencha com valores
lidos pelo teclado.

No final, mostre a
matriz na tela, com a
formatação correta.

OBS: Desafio feito em conjunto do Professor.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para {l},{c}: '))
print('='*50)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()