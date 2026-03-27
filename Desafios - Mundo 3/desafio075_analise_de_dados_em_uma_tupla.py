"""
Desafio 075: Desenvolva um
programa que leia
quatro valores pelo
teclado e guarde-os
em uma tupla. No final,
mostre:

A) Quantas vezes
apareceu o valor 9.

B) Em que posição foi
digitado o primeiro
valor 3.

C) Quais foram os
números pares.
"""
v = int(input('Primeiro Valor: ')),int(input('Segundo Valor: ')),int(input('Terceiro Valor: ')),int(input('Último Valor: '))
print(f'Valores digitados: {v}')
print(f'O número 9 apareceu {v.count(9)} vezes')
if 3 in v:
    print(f'O número 3 apareceu na {v.index(3)+1} posição')
else:
    print('O número 3 não foi digitado.')
print('Pares: ',end='')
for c in v:
    if c % 2 == 0:
        print(c,end=' ')