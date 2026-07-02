"""
Desafio 098: Faça um programa
que tenha uma função
chamada contador(),
que recebe três
parâmetros: início, fim
e passo e realize a
contagem.

Seu programa tem que
realizar três
contagens através da
função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem
personalizada.
"""
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo = passo * (-1)
    else:
        if passo == 0:
            passo = 1
    print('='*40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    for c in range(inicio, fim+1, passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    for c in range(inicio, fim-1, -passo):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('FIM')


contador(1,10,1)
contador(10,0,1)
print('='*40)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)