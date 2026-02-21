"""
Desafio 064: Crie um programa
que leia vários
números inteiros pelo
teclado. O programa só
vai parar quando o
usuário digitar o valor
999, que é a condição
de parada. No final,
mostre quantos
números foram
digitados e qual foi a
soma entre eles.
(desconsiderando o flag)
"""
n = 0
cont = 0
s = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 Para encerrar]: '))
    if n != 999:
        s += n
        cont += 1
print('Soma dos números digitados: {}'.format(s))
print('Total de números digitados: {}'.format(cont))