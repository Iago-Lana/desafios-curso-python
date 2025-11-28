"""
Desafio 044: Elabore um programa
que calcule o valor a ser
pago por um produto,
considerando o seu
preço normal e condição
de pagamento:

- À vista dinheiro/cheque: 10% de desconto

- À vista no cartão: 5% de desconto

- Em até 2x no cartão: preço normal

- 3x ou mais no cartão: 20% de juros
"""
produto = float(input('Preço do produto: '))
desconto1 = produto * 0.10
desconto2 = produto * 0.05
juros = produto * 0.20
print('''
=========================================================
FORMAS DE PAGAMENTO:
                                       
[1] À vista no dinheiro/cheque ----> [10% de desconto]
      
[2] À vista no cartão -------------> [5% de desconto]
       
[3] Em até 2x no cartão -----------> [Preço normal]
          
[4] Em 3x ou mais no cartão -------> [Juros de 20%]    
=========================================================''')
opcao = int(input('Escolha a forma de pagamento: '))
if opcao == 1:
    print('À vista no dinheiro/cheque você tera 10% de desconto.')
    print('O produto estava por R${:.2f} com o desconto ficou R${:.2f}'.format(produto,produto-desconto1))
elif opcao == 2:
    print('À vista no cartão você tera 5% de desconto')
    print('O produto estava por R${:.2f} com o desconto ficou R${:.2f}'.format(produto,produto-desconto2))
elif opcao == 3:
    print('Em 2x no cartão produto continua em seu preço padrão')
    print('Você ira pagar duas parcelas de R${:.2f}'.format(produto/2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Em 3x ou mais será aplicado juros de 20% ao produto')
    print('Você ira pagar {} parcelas de R${:.2f}'.format(parcelas,(produto+juros)/parcelas))
    print('Seu produto de {} ira custar R${:.2f} no final'.format(produto,produto+juros))
else:
    print('Opção invalida, tente novamnete.')
