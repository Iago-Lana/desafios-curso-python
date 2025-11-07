"""
Desafio 031: Desenvolva um programa que pergunte a distãncia de uma viagem em km.
calcule o preço da passagem, cobrando, R$0,50 por Km para viagens de até 200km
e R$0,45 para viagens mais longas
"""
distãncia = float(input('Qual será a distãncia da viagem? '))
if distãncia <= 200:
    print('O preço da viagem será R${:.2f}'.format(0.50*distãncia))
else:
    print('O preço da viagem será R${:.2f}'.format(0.45*distãncia))    