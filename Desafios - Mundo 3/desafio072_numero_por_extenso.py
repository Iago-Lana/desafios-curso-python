"""
Desafio 072: Crie um programa
que tenha uma Tupla
totalmente
preenchida com uma
contagem por
extenso, de zero até
vinte.

Seu programa deverá
ler um número pelo
teclado (entre 0 e 20)
e mostrá-lo por
extenso
"""
n = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
r = int(input('Digite um número [Entre 0 e 20]: '))
while r < 0 or r >= 21:
    r = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número --> {n[r]}')
