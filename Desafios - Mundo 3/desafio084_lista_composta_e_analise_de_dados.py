"""
Desafio 084: Faça um programa
que leia o nome e peso
de várias pessoas,
guardando tudo em
uma lista. No final,
mostre:

A) Quantas pessoas
foram cadastradas.

B) Uma listagem com as
pessoas mais
pesadas.

C) Uma listagem com as
pessoas mais leves.
"""
pessoas = list()
dados = list()
maior = menor = cont = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if cont == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    cont += 1
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if r == 'N':
        break
print('='*60)
print(f'Ao todo {cont} pessoas foram cadastradas.')
print(f'Maior peso digitado {maior}Kg. Peso de: ',end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print(f'\nMenor peso digitado {menor}Kg. Peso de: ',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')