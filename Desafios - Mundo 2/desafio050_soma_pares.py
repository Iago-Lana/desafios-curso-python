"""
Desafio 050: Desenvolva um
programa que leia seis
números inteiros e
mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar,
desconsidere-o
"""
p = 0
s = 0
for c in range(1,7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n%2==0:
        p += 1
        s += n
print('Ao todo são {} números pares.'.format(p))
print('Resultado: {}'.format(s))
