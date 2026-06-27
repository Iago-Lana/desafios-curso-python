"""
Desafio 097: Faça um programa
que tenha uma função
chamada escreva(),
que receba um texto
qualquer como
parâmetro e mostre
uma mensagem com
tamanho adaptável.

ex:
escreva('Olá, Mundo!')

saída:
============
 Olá, Mundo
============
"""
def escreva(texto):
    print(f'=' * len(texto) + '='*2)
    print(f'{'':>1}{texto}')
    print(f'=' * len(texto) + '='*2)


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
