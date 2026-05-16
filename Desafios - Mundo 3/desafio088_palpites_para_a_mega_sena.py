"""
Desafio 088: Faça um programa
que ajude um jogador
da MEGA SENA a criar
palpites. O programa
vai perguntar quantos
jogos serão gerados e
vai sortear 6 números
entre 1 e 60 para cada
jogo, cadastrando
tudo em uma lista
composta
"""
from random import randint
from time import sleep
jogos = int(input('Quantos jogos deseja sortear? '))
print('='*15,f'SORTEANDO {jogos} JOGOS','='*15)
for c in range(jogos):
    lista = []
    cont = 0
    while True:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont == 6:
            break
        lista.sort()
    print(f'Jogo {c+1}: {lista}')
    sleep(1)
print('='*15, 'BOA SORTE', '='*22)