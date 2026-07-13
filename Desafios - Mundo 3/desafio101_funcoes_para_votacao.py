"""
Desafio 101: Crie um programa
que tenha uma função
chamada voto() que
vai receber como
parãmetro o ano de
nascimento de uma
pessoa, retornando
um valor literal
indicando se uma
pessoa tem voto
negado, opcional ou
obrigatório nas
aleições.
"""
from datetime import date


def voto(nas):
    nas = date.today().year - nas
    print(f'Com {nas} anos: ',end='')
    if nas < 16:
        return 'VOTO NEGADO'
    elif 16 <= nas < 65:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'


nascimento = int(input('Ano de nascimento: '))
print(voto(nascimento))
