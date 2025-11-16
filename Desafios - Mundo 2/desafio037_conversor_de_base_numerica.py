"""
Desafio 037: Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:

-1 para Binário
-2 para Octal
-3 para Hexadecimal
"""
n = int(input('Digite um número inteiro: '))
print('''Escolha uma base de conversão: 
[1] Para Binário
[2] Para Octal
[3] Para Hexadecimal ''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Binário é igual a {}'.format(n,bin(n)[2:]))
elif opcao == 2:
    print('{} Convertido para Octal é igual a {}'.format(n,oct(n)[2:]))
elif opcao == 3:
    print('{} Convertido para Hexadecimal é igual a {}'.format(n,hex(n)[2:]))
else:
    print('Opção invalida. Tente novamente.')

"""
Nota: Programa feito junto com o professor por orientação do mesmo.
"""