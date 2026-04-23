"""
Desafio 082: Crie um programa
que vai ler vários
números e colocar em
uma lista.

Depois disso, crie duas
listas extras que vão
conter apenas os
valores pares e os
valores ímpares
digitados,
respectivamente.

Ao final, mostre o
conteúdo das três
listas geradas
"""
lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    lista.append(n)
    while r != 'S' and r != 'N':
         r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if n%2 == 0:
         lista_par.append(n)
    if n%2 == 1:
         lista_impar.append(n)
    if r in 'N':
         break
print('='*40)
print(f'Lista COMPLETA: {lista}')
print(f'Lista PAR: {lista_par}')
print(f'Lista ÍMPAR: {lista_impar}')
        