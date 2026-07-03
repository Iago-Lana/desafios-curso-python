"""
Desafio 099: Faça um programa
que tenha uma função
chamada maior(), que
receba vários
parâmetros com
valores inteiros.

Seu programa tem que
analisar todos os
valores e dizer qual
deles é o maior.
"""
from time import sleep


def maior(* num):
    if num != ():
        m = max(num)
    else:
        m = 0
    print('='*50)
    print('Analisando os números digitados...')
    for c in num:
        print(c,end=' ',flush=True)
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo',end='')
    print(f'\nO maior valor digitado é {m}')


maior(2,9,4,5,7,1)
maior(4,0,7)
maior(1,2)
maior(6)
maior()