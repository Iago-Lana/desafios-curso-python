"""
Desafio 091: Crie um programa
que gerencie o
aproveitamento de um
jogador de futebol. O
programa vai ler o
nome do jogador e
quantas partidas ele
jogou. Depois vai ler a
quantidade de gols
feitos em cada
partida. No final, tudo
isso será guardado em
um dicionário,
incluindo o total de
gols feitos durante o campeonato
"""
jogador = dict()
gols = list()
tot = 0
jogador['Nome'] = str(input('Nome do jogador: '))
partida = int(input('Quantas partidas ele jogou? '))
for c in range(partida):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogador['Gols'] = gols
for t in gols:
    tot += t
jogador['Total'] = tot
print('='*60)
print(jogador)
print('='*60)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('='*60)
print(f'O Jogador {jogador['Nome']} jogou {partida} partidas.')
for p, g in enumerate(gols):
    print(f'{'=>':>5} Na partida {p}, fez {g} gols.')
print(f'Foi um total de {tot} gols.')
