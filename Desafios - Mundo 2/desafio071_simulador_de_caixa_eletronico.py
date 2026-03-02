"""
Desafio 071: Crie um programa
que simule o
funcionamento de um
caixa eletrônico. No
início, pergunte ao
usuário qual será o
valor a ser sacado
(número inteiro) e o
programa vai informar
quantas cédulas de
cada valor serão
entregues.

OBS: Considere que o
caixa possui cédulas
de R$50, R$20, R$10 e
R$1.
"""
cont = 0
atual = 50
n = int(input('Qual valor deseja sacar? '))
while True:
    cont = 0
    if n >= atual:
        while n >= atual:
            n -= atual
            cont += 1
        print(f'Total de {cont} cédulas de R${atual}')
    else:
        if atual == 50:
            atual = 20
        else:
            if atual == 20:
                atual = 10
            else:
                if atual == 10:
                    atual = 1
    if n == 0:
        break