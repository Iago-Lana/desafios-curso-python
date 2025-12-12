"""
Desafio 052: Faça um programa
que leia um número
inteiro e diga se ele é
ou não um número primo.
"""
p = 0
n = int(input('Digite um número inteiro: '))
for c in range(1,n+1):
    if n%c == 0 and n%n == 0:
        p += 1
print('O número {} foi divisível {} vezes'.format(n,p))
if p == 2:
    print('{} É um número primo'.format(n))
else:
    print('{} Não é um número primo'.format(n))

  