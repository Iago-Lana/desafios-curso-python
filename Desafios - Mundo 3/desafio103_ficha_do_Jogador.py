"""
Desafio 103: Faça um programa
que tenha uma função
chamada ficha(), que
receba dois parâmetros
opcionais: o nome de um
jogador e quantos gols
ele marcou.
"""


def ficha(nome='<Desconhecido>', gols=0):
    print(f'O Jogador {nome} fez {gols} gols(s) no campeonato.')


Jogador = str(input('Nome do Jogador: '))
Gol = str(input('Número de Gols: '))
if Gol.isnumeric():
    Gol = int(Gol)
else:
    Gol = 0

if Jogador.strip() == '':
    ficha(gols= Gol)
else:
    ficha(Jogador, Gol)