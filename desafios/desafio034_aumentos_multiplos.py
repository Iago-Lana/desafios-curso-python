"""
Desafio 034: Escreva um programa que
pergunte o salário de
um funcionário e
calcule o valor do seu
aumento.

para salários
superiores a R$1.250,00, calcule um aumento de 10%.

para os inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input('Qual seu salário atual? R$'))
if salario > 1250:
    salario = salario * (1 + 10/100)
    print('Seu novo salário será R${:.2f}'.format(salario))
else:
    salario <= 1250
    salario = salario * (1 + 15/100)
    print('Seu novo salário será R${:.2f}'.format(salario))
