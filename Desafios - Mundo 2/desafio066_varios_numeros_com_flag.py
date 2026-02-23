"""
Desafio 066: Crie um programa
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
s = 0
cont = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Soma dos números digitados: {s}')
print(f'Total de números digitados: {cont}')