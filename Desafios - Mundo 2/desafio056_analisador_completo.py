"""
DEsafio 056: Desenvolva um
programa que leia o
nome, idade e sexo de
4 pessoas. No final do programa, mostre:

> A média de idade do
grupo.

> Qual é o nome do
homem mais velho.

> Quantas mulheres têm menos de 20
anos
"""
media = 0
homem_velho = ''
mais_velho = 0
mulher_menor20 = 0
for c in range(1,5):
    print('====== {}ª Pessoa ======'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    media += idade
    sexo = str(input('Sexo [M/F]: ')).upper()
    if c == 1 and sexo == 'M':
        mais_velho = idade
        homem_velho = nome
    else:
        if idade > mais_velho and sexo == 'M':
            mais_velho = idade
            homem_velho = nome
    if sexo == 'F' and idade < 20:
         mulher_menor20 += 1
print('A média de idade do grupo é {:.1f} anos'.format(media/4))
print('O homem mais velho se chama {} e tem {} anos'.format(homem_velho,mais_velho))
print('Ao todo {} mulheres tem menos de 20 anos.'.format(mulher_menor20))
