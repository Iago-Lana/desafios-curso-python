"""
Desafio 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

considere: US$1,00 = R$3,27

"""
R = float(input('Quanto dinheiro você tem na sua carteira? R$'))
print('Com R${} você pode comprar US${:.2f}'.format(R, R/3.27))