"""
Desafio 012: Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

"""
produto = float(input('Qual o preço do produto? R$'))
desconto = 5/100*produto
print('O produto que custava R${}, na promoção de 5% de desconto vai custar R${:.2f}'.format(produto, produto-desconto))