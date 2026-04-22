"""
Desafio 081: Crie um programa
que vai ler vários
números e colocar em uma lista.

depois disso, mostre:

A) Quantos números
foram digitados.

B) A lista de valores,
ordenada de forma
decrescente.

C) Se o valor 5 foi
digitado e está ou não
na lista.
"""
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while r != 'S' and r != 'N':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if r in 'N':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A ordem decrescente da lista é {lista}')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')