"""
Desafio 061: Refaça o desafio
051, lendo o primeiro
termo e a razão de uma
PA, mostrando os 10
primeiros termos da
progressão usando a
estrutura while
"""
print('''===============================
Progressão Aritmética v2.0
===============================''')

t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
while c < 10:
    print('{} ->'.format(t),end=' ')
    t += r
    c += 1
print('FIM')
