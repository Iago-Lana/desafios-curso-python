"""
Desafio 074: Crie um programa
que vai gerar cinco
números aleatórios e
colocar em uma tupla.

Depois disso, mostre a
listagem de números
gerados e também
indique o menor e o
maior valor que estão
na tupla.
"""
from random import randint
t = ()
maior = 0
menor = 0
for c in range(1,6):
    s = (randint(1,10)),
    t += s
    if c == 1:
        maior = s
        menor = s
    else:
        if s > maior:
            maior = s
        if s < menor:
            menor = s
print(f'Números sorteados: {t}')
print(f'Maior número: {maior[0]}')
print(f'Menor número: {menor[0]}')