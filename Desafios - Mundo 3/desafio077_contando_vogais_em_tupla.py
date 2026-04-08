"""
DEsafio 077: Crie um programa
que tenha uma tupla
com várias palavras
(Não usar acentos).
Depois disso, você
deve mostrar, para
cada palavra, quais
são as suas vogais.
"""
lista = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')
v = ('a', 'e', 'i', 'o','u')
for c in lista:
    vs = ''
    for d in c:
        if d in v:
            vs += d
    print(f'Na palavra {c.upper()} temos: {vs.replace('',' ')}')