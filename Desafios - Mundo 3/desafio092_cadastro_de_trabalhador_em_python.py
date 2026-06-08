"""
Desafio 092: Crie um programa
que leia nome, ano de
nascimento e carteira
de trabalho e
cadastre-os (com
idade) em um dicionário
se por acaso a CTPS
for diferente de zero,
o dicionário receberá
também o ano de
contratação e o
salário. Calcule e
acrescente, além da
idade, com quantos
anos a pessoa vai se
aposentar
"""
from datetime import date
cadastro = dict()
ano = date.today().year
aposentadoria = 35
cadastro['Nome'] = str(input('Nome: '))
cadastro['Idade'] = ano - int(input('Ano de nascimento: '))
cadastro['Ctps'] = int(input('Carteira de trabalho (0 Não tem): '))
if cadastro['Ctps'] != 0:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = cadastro['Contratação'] + aposentadoria + cadastro['Idade'] - ano
print('='*40)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')