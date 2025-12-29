"""
Desafio 058: Melhore o jogo do desafio 028 
onde o computador vai "Pensar" em um 
número entre 0 e 10. só
que agora o jogador vai
tentar adivinhar até
acertar, mostrando no
final quantos palpites
foram necessários
para vencer.
"""
from random import randint
total = 1
n = randint(0,10)
print('='*35)
print('PENSEI EM UM NÚMERO ENTRE 0 E 10. \nCONSEGUE ACERTAR QUAL?')
print('='*35)
t = int(input('Digite sua tentativa: '))
while t != n:
    total += 1
    if t > n:
        t = int(input('O número que pensei é menor, tente novamente: '))
    elif t < n:
        t = int(input('O número que pensei é maior, tente novamente: '))
if t == n:
    print('PARABÉNS! Você acertou eu estava pensando no número {}'.format(n))
print('TOTAL DE TENTATIVAS: {}'.format(total))
