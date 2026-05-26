"""
Desafio 090: Faça um programa
que leia nome e média
de um aluno,
guardando também a
situação em um
dicionário. No final,
mostre o conteúdo da
estrutura na tela
"""
aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Qual a média de {aluno['Nome']}: '))
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
if aluno['Média'] >= 7:
    print('Situação igual a Aprovado')
else:
    print('Situação igual a Reprovado')