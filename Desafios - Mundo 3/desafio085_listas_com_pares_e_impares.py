"""
Desafio 085: Crie um programa
onde o usuário possa
digitar sete valores
numéricos e
cadastre-os em uma
lista única que
mantenha separados
os valores pares e
ímpares. No final,
mostre os valores
pares e ímpares em
ordem crescente.
"""
numeros = [],[]
for c in range(0,7):
    n = int(input(f'Digite o {c+1}° número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('='*50)
print(f'Números Pares: {numeros[0]}')
print(f'Números Ímpares: {numeros[1]}')
