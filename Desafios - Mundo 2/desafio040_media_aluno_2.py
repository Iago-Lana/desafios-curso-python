"""
Desafio 040: Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensangem no final,
de acordo com a média atingida:

- Média abaixo de 5.0:
REPROVADO.

- Média entre 5.0 e 6.9:
RECUPERAÇÃO.

- Média 7.0 ou superior:
"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segundo nota: '))
media = (n1 + n2) /2
if media < 5:
    print('Suas notas foram {} e {}, sendo assim sua média foi {}'.format(n1,n2,media))
    print('Aluno REPROVADO')
elif 7 > media >= 5:
    print('Suas notas foram {} e {}, sendo assim sua média foi {}'.format(n1,n2,media))
    print('Aluno está de RECUPERAÇÃO')
elif media >= 7:
    print('Suas notas foram {} e {}, sendo assim sua média foi {}'.format(n1,n2,media))
    print('Aluno APROVADO')
