"""
Desafio 039: Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo
que falta ou que passou do prazo.
"""
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('Você ainda não precisa de alistar.')
    print('Seu alistamento será daqui {} anos.'.format(18-idade))
elif idade == 18:
    print('Você já pode e deve fazer seu alistamento.')
elif idade > 18:
    print('Já passou o tempo do seu alistamento.')
    print('Seu alistamento foi a {} anos atrás.'.format(idade-18))
