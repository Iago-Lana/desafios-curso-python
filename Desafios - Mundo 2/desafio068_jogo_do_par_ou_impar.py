"""
Desafio 068: Faça um programa
que jogue par ou ímpar
com o computador. O
jogo só será
interrompido quando o
jogador PERDER,
mostrando o total de
vitórias consecutivas
que ele conquistou no
final do jogo
"""
from random import randint
v = 0
while True:
    print('='*30,'JOGO DO PAR OU ÍMPAR','='*30)
    n = int(input('Digite sua jogada [1 a 10]: '))
    if n > 10:
        n = int(input('Jogada invalida, tente novamente: '))
    c = randint(1,10)
    r = str(input('PAR OU ÍMPAR? [P/I] ')).upper().strip()
    j = n + c
    if j % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {c}. Total {j} [PAR]')
        if r == 'P':
            print('='*30)
            print('Você GANHOU! \nVamos jogar novamente...')
            v += 1
        else:
            print('='*30)
            print('Você PERDEU!')
            print('='*30)
            break
    else:
        print(f'Você jogou {n} e o computador jogou {c}. Total {j} [ÍMPAR]')
        if r == 'I':
            print('='*30)
            print('Você GANHOU! \nVamos jogar novamente...')
            v += 1
        else:
            print('='*30)
            print('Você PERDEU!')
            print('='*30)
            break
print(f'Jogo finalizado. \n{v} Vitórias Consecutivas.')