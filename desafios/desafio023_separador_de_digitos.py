"""
Desafio 023: Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos digitos separados.

ex:
Digite um número: 1834
unidade:4
dezena:3
centena:8
milhar:1
"""
num = int(input('Digite um número entre 0 a 9999: '))
u = num % 10
print('Unidade: {}'.format(u))
d = (num // 10) % 10
print('Dezena: {}'.format(d))
c = (num // 100) % 10
print('Centena: {}'.format(c))
m = (num // 1000) % 10
print('Milhar: {}'.format(m))
