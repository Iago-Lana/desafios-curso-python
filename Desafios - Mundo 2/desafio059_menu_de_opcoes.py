"""
Desafio 059: Crie um programa
que leia dois valores e
mostre na tela:

[1] somar
[2] multiplicação
[3] maior
[4] novos números
[5] sair do programa
"""
opcao = 0
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
while opcao != 5:
    print(''' ====== MENU DE OPÇÕES =============
[1] SOMA
[2] MULTIPLICAÇÃO
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA''')
    print('='*35)
    if opcao > 5:
        print('OPÇÃO INVALIDA.')
    if opcao == 1:
        print('>>>> {} + {} = {}'.format(n1,n2,n1+n2))
    elif opcao == 2:
        print('>>>> {} X {} = {}'.format(n1,n2,n1*n2))
    elif opcao == 3:
        if n1 > n2:
            print('{} É maior que {}'.format(n1,n2))
        elif n2 > n1:
            print('{} É maior que {}'.format(n2,n1))
        else:
            print('OS VALORES DIGITADOS SÃO IGUAIS.')
    elif opcao == 4:
        print('DIGITE OS NOVOS VALORES')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    opcao = int(input('Digite a opção desejada: '))
print('SAINDO DO PROGRAMA...')
