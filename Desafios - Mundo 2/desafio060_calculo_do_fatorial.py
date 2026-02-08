"""
Desafio 060: Faça um programa
que leia um número
qualquer e mostre o
seu fatorial.

ex:
5! = 5x4x3x2x1 = 120
"""
print('Digite um número para ver seu fatorial')
n = int(input('Digite o número desejado: '))
c = n
t = 1
print(end='' '{}! = {} '.format(n,n))
while c > 0:
    t = c * t
    c -= 1
    if n == 1:
        print('X 1', end=' ')
    if c > 0:
        print('X {}'.format(c), end=' ')
    else:
        print('= {}'.format(t), end=' ')
