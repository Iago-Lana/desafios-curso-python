"""
Desafio 069: Crie um programa
que leia a idade e o
sexo de várias
pessoas. A cada
pessoa cadastrada, o
programa deverá
perguntar se o usuário
quer ou não continuar.
No final, mostre:

A) Quantas pessoas
   tem mais de 18 anos.

B) Quantas homens
   foram cadastrados.

C) Quantas mulheres
   tem menos de 20 anos.
"""
maior18 = 0
tothomem = 0
mulhermenos20 = 0
while True:
    print('='*30)
    print('CADASTRO DE PESSOAS')
    print('='*30)
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if sexo == 'M':
        tothomem += 1
    elif idade < 20:
        mulhermenos20 += 1
    else:
        while sexo != 'M' and sexo != 'F':
            sexo = str(input('Sexo [M/F]: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar [S/N] '))
    if r == 'N':
        break
print('='*40)
print(f'Ao todo {maior18} pessoas tem mais de 18 anos')
print(f'{tothomem} homens foram cadastrados')
print(f'{mulhermenos20} mulheres tem menos de 20 anos.')
print('='*40)
