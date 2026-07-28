"""
Desafio 106: Faça um mini-sistema
que utilize o
interactive Help do
Python. O usuário vai
digitar o comando e o
manual vai aparecer.
Quando o usuário digitar
a palavra 'FIM', o
programa se encerrará.

OBS: use cores.
"""
from time import sleep

cores = ('\033[32m', #  0 verde
         '\033[34m', #  1 ciano
         '\033[35m', #  2 magenta
         '\033[31m', #  3 vermelho
         '\033[0m'  #   4 Sem cor
        )


def ajuda(n):
    titulo(f'Acessando o manual do comando "{n}"',1)
    sleep(1)
    print(cores[2])
    help(n)
    print(cores[4])


def titulo(texto, cor=0):
    tam = len(texto) + 2
    print('='*tam)
    print(cores[cor],end='')
    print(  texto)
    print(cores[4],end='')
    print('='*tam)


resp = ''
while True:
    titulo('Sistema de Ajuda PyHelp',0)
    comando = str(input('Função ou Biblioteca ("FIM" para Encerrar): '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('<- PROGRAMA ENCERRADO VOLTE SEMPRE! ->')