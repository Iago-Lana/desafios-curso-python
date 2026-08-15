"""
Desafio 115: Crie um pequeno
sistema modularizado
que permita cadastrar
pessoas pelo seu nome
e idade em um arquivo de
texto simples.

O sistema só vai ter 2
opções: cadastrar uma
nova pessoa e listar
todas as pessoas
cadastradas.
"""

from sistema import mostrarmenu, mostrarcadastro, cadastro

while True:
    mostrarmenu()
    try:
        r = int(input('\033[32mSua Opção: \033[0m'))
        print('='*50)
    except ValueError:
        print('\033[31mERRO: Apenas números inteiros são aceitos\033[0m')
    else:
        if r == 1:
            mostrarcadastro()
        elif r == 2:
            cadastro()
        elif r == 3:
            print('<= \033[34mVOLTE SEMPRE\033[0m =>'.center(55))
            break
        else:
            print('\033[31mERRO: Digite um valor entre 1 e 3\033[0m')