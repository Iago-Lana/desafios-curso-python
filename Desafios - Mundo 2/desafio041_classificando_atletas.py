"""
Desafio 041: A confederação nacional de natação 
precisa de um programa que leia o ano de nascimento um atleta e mostre
sua categoria, de
acordo com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infaltil
- Até 19 anos: Junior
- Até 25 anos: Sênior
- Acima: Master
"""
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: MIRIM')
elif idade <= 14:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: INFALTIL')
elif idade <= 19:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: SÊNIOR')
else:
    print('O atleta tem {} anos.'.format(idade))
    print('Categoria: MASTER')   