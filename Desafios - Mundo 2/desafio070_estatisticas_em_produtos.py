"""
Crie um programa
que leia o nome e o
preço de vários
produtos. O programa
deverá perguntar se o
usuário vai continuar.
No final, mostre:

A) Qual é o total gasto
   na compra.

B) Quantos produtos
   custam mais de
   R$1000.

C) Qual é o nome do produto mais barato.
"""
totalcompra = 0
tot1000 = 0
barato = ''
menor = 0
cont = 0
print('='*30)
print('     BEM VINDO (A)\n     FAÇA SUAS COMPRAS')
print('='*30)
while True:
    n = str(input('Nome do produto: ')).capitalize()
    p = float(input('Preço: '))
    if cont == 0:
        menor = p
        barato = n
    cont += 1
    totalcompra += p
    if p < menor:
        menor = p
        barato = n
    if p > 1000:
        tot1000 += 1
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    print('='*30)
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if r == 'N':
        break
print('='*30,'FIM DO PROGRAMA','='*30)
print(f'O total da compra foi: R${totalcompra:.2f}')
print(f'Ao todo {tot1000} produtos custam mais de R$1000')
print(f'O produto mais barato foi {barato} custando R${menor:.2f}')
