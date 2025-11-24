"""
Desafio 042: Refaça o desafio 035 dos triângulos,
acrescentando o recurso de mostrar
que tipo de triângulo será formado:

- Equilátero: Todos os lados iguias

- Isósceles: Dois lados iguais

- Escaleno: Todos os lados diferentes
"""
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo.')
    if r1 == r2 == r3:
        print('Tipo de triângulo: EQUILATERO')
    elif r1 == r2 or r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1 or r3 == r2:
        print('Tipo de triângulo: ISÓSCELES')
    elif r1 != r2 != r3 != r1:
        print('Tipo de triângulo: ESCALENO')
else:
    print('Os segmentos acima não podem formar um triângulo.')
