"""
Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto
"""
ano = int(input('Digite um ano para saber se ele é bissexto ou não: '))
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('{} É um ano BISSEXTO.'.format(ano))
else:
    print('{} Não é um ano BISSEXTO.'.format(ano))
    