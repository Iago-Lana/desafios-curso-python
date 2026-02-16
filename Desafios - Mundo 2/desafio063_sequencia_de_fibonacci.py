"""
Desafio 063: Escreva um
programa que leia um
número n inteiro
qualquer e mostre na
tela os n primeiros
elementos de uma
Sequência de
Fibonacci
"""
print('='*30)
print('   SEQUÊNCIA DE FIBONACCI')
print('='*30)
f = int(input('Quantos termos da sequência que você deseja ver? '))
n1 = 0
n2 = 1
print('{} -> {}'.format(n1,n2),end=' ')
while f > 2:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    f -= 1
    print('-> {}'.format(n3),end=' ')
print('-> FIM')