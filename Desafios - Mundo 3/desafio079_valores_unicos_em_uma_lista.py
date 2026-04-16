"""
Desafio 079: Crie um programa
onde o usuário possa
digitar vários valores
numéricos e
cadastre-os em uma
lista. Caso o número já
exista lá dentro, ele
não será adicionado.
No final, serão
exibidos todos os
valores únicos
digitados, em ordem
crescente.
"""
valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        print('Valor adicionado com sucesso')
        valores.append(valor)
    else:
        if valor in valores:
            print('Valor já foi adicionado anteriomente')
    r = str(input('Deseja continuar? [S/N] ')).upper()
    if r in 'N':
        break
valores.sort()
print('='*100)
print(f'Valores digitados em ordem crescente --> {valores}')