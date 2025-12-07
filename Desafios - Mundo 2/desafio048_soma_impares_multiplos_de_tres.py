"""
Desafio 048: Faça um programa
que calcule a soma
entre todos os
números ímpares que são multiplos de três e
que se encontram no
intervalo de 1 até 500
"""
qi = (500+1)/2 - 1/2
s = 0
n = 1
for n in range(1,501):
    if n%3==0 and n%2!=0:
        s = s + n
print('A soma dos {:.0f} números é {}.'.format(s/qi,s))
