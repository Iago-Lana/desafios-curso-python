"""
Desafio 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

"""

cit = str(input('Onde você nasceu? ')).strip()
print('SANTO' in cit[0:5].upper())

