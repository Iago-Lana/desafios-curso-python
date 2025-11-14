"""
Desafio 016: Crie um programa que leia um número real e mostre na tela a sua porção inteira.

"""
from math import trunc
num = float(input('Digite um número real: '))
print('O número {} tem como parte inteira {}'.format(num, trunc(num)))