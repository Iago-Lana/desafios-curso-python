"""
Desafio 045: Crie um programa que jogue
jokenpô com você.
"""
from random import randint
print('''
J O K E N P Ô
==============
[1] PEDRA
[2] PAPEL
[3] TESOURA
==============''')
opcao = int(input('Qual sua jogada? '))
computador = randint(1,3)
if opcao == 1:
    print('Você escolheu PEDRA')
    if computador == 1:
        print('Computador escolheu PEDRA')
        print('EMPATE!')
    elif computador == 2:
        print('Computador escolheu PAPEL')
        print('Você PERDEU!')
    elif computador == 3:
        print('Computador escolheu TESOURA')
        print('Parabéns! Você GANHOU!')    

if opcao == 2:
    print('Você escolheu PAPEL')
    if computador == 1:
        print('Computador escolheu PEDRA')
        print('Parabéns! você GANHOU!')
    elif computador == 2:
        print('Computador escolheu PAPEL')
        print('EMPATE!')
    elif computador == 3:
        print('Computador escolheu TESOURA')
        print('Você PERDEU!')

if opcao == 3:
    print('Você escolheu TESOURA')
    if computador == 1:
        print('Computador escolheu PEDRA')
        print('Você PERDEU')
    elif computador == 2:
        print('Computador escolheu PAPEL')
        print('Parabéns! você GANHOU!')
    elif computador == 3:
        print('Computador escolheu TESOURA')
        print('EMPATE!')

if opcao > 3:
    print('Opção INVALIDA')
                 

