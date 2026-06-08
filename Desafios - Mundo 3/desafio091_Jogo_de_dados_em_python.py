"""
Desafio 091: Crie um programa
onde 4 jogadores
joguem um dado e
tenham resultados em
um dicionário. No final,
coloque esse
dicionário em ordem,
sabendo que o
vencedor tirou o maior
número no dado
"""
from random import randint
from operator import itemgetter
from time import sleep
jogadores = dict()
for c in range(1,5):
    jogadores[f'Jogador{c}'] = randint(1,6)
for k,v in jogadores.items():
    print(f'{k} Tirou {v}')
    sleep(1)
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print('='*30)
print('Ranking dos Jogadores: ')
print('='*30)
for l, p in enumerate(ranking):
    print(f'{l+1}° Lugar: {p[0]} com {p[1]}')
    sleep(1)