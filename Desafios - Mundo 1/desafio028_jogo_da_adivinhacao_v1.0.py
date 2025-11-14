"""
Desafio 028: Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

o programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
n = random.randint(0,5)
tentativa = int(input('Digite sua tentativa: '))
if tentativa == n:
    print('VOCÊ VENCEU! PARABENS!')
else:
    print('VOCÊ PERDEU! \neu estava pensando no número {}'.format(n))
            