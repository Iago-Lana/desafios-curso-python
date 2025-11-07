"""
Desafio 029: Escreva um programa que leia a
velocidade de um carro.
se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado.

a multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = float(input('Digite a velocidade: '))
if velocidade > 80:
    print('MULTADO! Você ultrapassou o limite de 80Km/h')
    print('E devera pagar uma multa no valor de R${}'.format((velocidade-80)*7))
else:
    print('Sua velociade está no limite aceitável.')    