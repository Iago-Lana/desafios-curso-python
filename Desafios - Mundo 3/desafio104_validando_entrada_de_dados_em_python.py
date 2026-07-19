""""
Desafio 104: Crie um programa
que tenha uma função
leiaInt(), que vai
funcionar de forma
semelhante à função
input() do Python, só
que fazendo a validação
para aceitar apenas um
valor numérico.

ex:
n = leiaInt('Digite um n')
"""


def leiaint(num):
    while True:
        print('='*40)
        v = str(input(num))
        if v.isnumeric():
            v = int(v)
            return v
        else:
            print("\033[31mERRO! Digite um número inteiro\033[0m")


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')