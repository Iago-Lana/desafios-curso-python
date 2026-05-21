"""
Desafio 089: Crie um programa
que leia nome e duas
notas de vários alunos
e guarde tudo em uma
lista composta. No
final, mostre um
boletim contendo a
média de cada um e
permita que o usuário
possa mostrar as
notas de cada aluno
invidividualmente.
"""
lista = []
while True:
    nome = str(input('Nome: ')).capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    aluno = nome,n1,n2,media
    lista.append(aluno)
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if r in 'N':
        break
print('='*40)
print('No. NOME', f'{'MEDIA':^20}')
print('='*28)
for p, me in enumerate(lista):
    print(f'{p:<3} {me[0]:<12} {me[3]:<10.1f}')
print('='*40)
while True:
    r = int(input('Deseja ver as notas de qual aluno? (999 para encerrar): '))
    for p, me in enumerate(lista):
        if r == p:
            print(f'{me[0]} Tem as seguintes notas: [{me[1]}, {me[2]}]')
            print('='*45)
    if r == 999:
        break
print('FINALIZANDO...')