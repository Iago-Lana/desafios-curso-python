"""
Desafio 036: Escreva um
programa para aprovar o empréstimo bancário
para a compra de uma casa.
o programa vai perguntar o valor da casa, o salário do
comprador e em quantos anos ele vai pagar.

Calcule o valor da
prestação mensal,
sabendo que ela não pode exceder 30% do salário
ou então o empréstimo será negado.
"""
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
ano = int(input('Em quantos anos você ira pagar? '))
prestacao = casa/(ano*12)
print('Ao pagar uma casa de R${:.2f} em {} anos a prestação mensal será de R${:.2f}'.format(casa,ano,prestacao))
if prestacao <= salario * 0.30:
    print('Emprestimo CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
