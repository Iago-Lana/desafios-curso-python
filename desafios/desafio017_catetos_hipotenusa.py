"""
Desafio 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

"""
from math import sqrt,pow
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
x = pow(co,2.0) + pow(ca,2.0)
h = sqrt(x)
print('A hipotenusa vai medir {:.2f}'.format(h))

