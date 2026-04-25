"""
Desafio 083: Crie um programa
onde o usuário digite
uma expressão
qualquer que use
parênteses. Seu
aplicativo deverá
analisar se a
expressão passada
está com os
parênteses abertos e
fechados na ordem
correta.
"""
expressao = []
n = str(input('Digite uma expressão: '))
for c in n:
    if c == '(':
        expressao.append(c)
    if c == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(())
            break
if len(expressao) == 0:
    print('Expressão Valida')
else:
    print('Expressão Inválida')
