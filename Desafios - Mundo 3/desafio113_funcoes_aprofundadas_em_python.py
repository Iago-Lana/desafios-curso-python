"""
Desafio 113: Reescreva a funcão
leiaInt() que fizemos no
desafio 104, incluindo
agora a possibilidade
da digitação de um
número de tipo inválido.
Aproveite e crie
também uma função
leiaFloat() com
mesma funcionalidade
"""


def leiaint(num):
    while True:
        print('='*40)
        try:
            n1 = int(input(num))
        except ValueError:
            print('\033[31mErrro: Digite um número Inteiro\033[0m')
        except KeyboardInterrupt:
            print('\033[31m\nO usuário preferiu não digitar esse número.\033[0m')
            return 0
        else:
            return n1


def leiafloat(num):
    while True:
        print('='*40)
        try:
            n2 = float(input(num))
        except ValueError:
            print('\033[31mErrro: Digite um número Real\033[0m')
        except KeyboardInterrupt:
            print('\033[31m\nO usuário preferiu não digitar esse número.\033[0m')
            return 0
        else:
            return n2


n = leiaint('Digite um número Inteiro: ')
r = leiafloat('Digite um número Real: ')
print(f'Você digitou o número inteiro {n} e o número real {r}')