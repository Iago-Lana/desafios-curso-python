"""
Desafio 094: Crie um programa
que leia nome, sexo e
idade de várias
pessoas, guardando
os dados de cada
pessoa em um
dicionário e todos os
dicionários em uma
lista. No final, mostre:

A) Quantas pessoas
foram cadastradas

B) A média de idade do
grupo.

C) Uma lista com todas
as mulheres.

D) Uma lista com todas
as pessoas com idade
acima da média.
"""
pessoa = dict()
lista = list()
media = 0
tot = 0
totm = ''
while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()
    if pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
        pessoa['Sexo'] = str(input('Sexo inválido, tente novamente [M/F]: ')).upper()
    pessoa['Idade'] = int(input('Idade: '))
    tot += pessoa['Idade']
    lista.append(pessoa.copy())
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if r in 'N':
        break
print('='*60)
print(f'- O grupo tem {len(lista)} pessoas.')
media = tot / len(lista)
print(f'- A média de idade do grupo é {media:.2f} anos.')
print('- As mulheres do grupo são: ',end='')
for c in lista:
    if c['Sexo'] == 'F':
        totm = c['Nome']
        print(f'[{totm}] ',end='')
print(f'\n- Lista das pessoas com idade acima da média: ')
for c in lista:
    if c['Idade'] > media:
        print()
        for k, v in c.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< FIM DO PROGRAMA >>')