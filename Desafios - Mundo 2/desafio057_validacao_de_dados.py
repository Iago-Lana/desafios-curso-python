"""
Desafio 057: Faça um programa
que leia o sexo de uma
pessoa, mas só aceite
os valores 'M' ou 'F'.
Caso esteja errado,
peça a digitação
novamente até ter um
valor correto.
"""
r = str(input('Informe seu sexo [M/F]: ')).upper().strip()
while r != 'M' and r != 'F':
    if r != 'M' and r != 'F':
        r = str(input('Valor digitado é inválido, tente novamente: ')).upper().strip()
print('Sexo {} validado com sucesso.'.format(r))
