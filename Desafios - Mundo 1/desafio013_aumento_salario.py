"""
Desafio 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

"""
salario = float(input('Qual o salário do funcionário? R$'))
aumento = 15/100*salario
print('O salário atual do funcionário é R${}, após o aumento de 15% ele passará a receber R${:.2f}'.format(salario, salario+aumento))