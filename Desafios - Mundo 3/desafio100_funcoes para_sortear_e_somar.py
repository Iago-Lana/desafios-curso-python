"""
Desafio 100: Faça um programa
que tenha uma lista
chamada números e
duas funções
chamadas sorteia() e
somaPar(). A primeira
função vai sortear 5
números e vai colocá-los
dentro da lista e a
segunda função vai
mostrar a soma entre
todos os valores
PARES sorteados pela
função anterior.
"""
from random import randint
from time import sleep


def sorteia(num):
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(0,5):
        n = randint(1,10)
        num.append(n)
        print(n,end=' ',flush=True)
        sleep(0.5)
    print('Pronto')


def somapar(num):
    s = 0
    for p in num:
        if p % 2 == 0:
            s += p
    print(f'Somando os valores pares de {num}, total: {s}')


numeros = list()
sorteia(numeros)
somapar(numeros)