"""
Desafio 051: Desenvolva um
programa que leia o primeiro termo e a
razão de uma PA. No
final, mostre os 10
primeiros termos dessa progressão
"""
p = int(input('Digite o primeiro termo: '))
r = int(input('Razão: '))
t = p + (10-1) * r
for c in range(p,t+1,r):
    print('{} ->'.format(c),end=' ')
print('FIM')
