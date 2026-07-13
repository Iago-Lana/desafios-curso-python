"""
Desafio 102: Crie um programa
que tenha uma função
fatorial() que receba
dois parâmetros: o
primeiro que indique o
número a calcular e o
outro chamado show,
que será um valor lógico
(opcional) indicando se
será mostrado ou não
na tela o processo de
calculo do fatorial.
"""


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número que será calculado
    :param show: (Opcional) Mostrar ou não a conta
    :return: O valor fatorial de um número num
    """
    f = 1
    for c in range(num, 1, -1):
        if show:
            print(f'{c} X ',end='')
            if c == 2:
                print('1 =',end=' ')
        f *= c
    return f


print(fatorial(5,show=True))
help(fatorial)
