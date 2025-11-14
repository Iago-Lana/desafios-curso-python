"""
Desafio 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin,cos,tan,radians
ângulo = float(input('Digite o ângulo que você deseja: '))
x = radians(ângulo)
print('O ângulo {} tem o SENO de {:.2f}'.format(ângulo, sin(x)))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(ângulo, cos(x)))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(ângulo, tan(x)))
