"""
Desafio 078: Faça um programa
que leia 5 valores
numéricos e guarde-
os em uma lista.

No final, mostre qual
foi o maior e menor
valor digitado e as
suas respectivas
posições na lista.

"""
valores = []
for c in range(0,6):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(valores)
menor = min(valores)
print('='*45)
print(f'Você digitou os seguintes valores: {valores}')
print(f'Maior número: {maior} nas posições ',end='')
for p, v in enumerate(valores):
    if v == maior:
        print(f'{p}... ',end='')
print(f'\nMenor número: {menor} nas posições ',end='')
for p, v in enumerate(valores):
    if v == menor:
        print(f'{p}... ',end='')