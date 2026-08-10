"""
Desafio 112: Dentro do pacote
utilidadesCeV que
criamos no desafio 111,
temos um módulo
chamado dado. Crie uma
função chamada
leiadinheiro() que seja
capaz de funcionar
como a função input(),
mas com uma validação
de dados para aceitar
apenas valores que
sejam monetários
"""
from utilidadesCeV import dado, moeda

p = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 30, 25)