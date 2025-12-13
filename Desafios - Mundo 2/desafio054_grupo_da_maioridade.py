"""
Desafio 054: Crie um programa
que leia o ano de
nascimento de sete
pessoas. No final,
mostre quantas
pessoas ainda não
atingiram a maioridade
e quantos já são
maiores.
"""
from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    n = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    if date.today().year-n >= 21:
        maior += 1
    else:
        menor += 1
print('{} Pessoas são maiores de idade.'.format(maior))
print('{} Pessoas ainda são menores de idade.'.format(menor))
