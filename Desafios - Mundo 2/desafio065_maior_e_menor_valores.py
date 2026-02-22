"""
Desafio 065: Crie um programa
que leia vários
números inteiros pelo
teclado. No final da
execução, mostre a
média entre todos os valores e qual foi o
maior e o menor
valores lidos. O
programa deve perguntar ao usuário
se ele quer ou não
continuar a digitar valores.
"""
n = 0
maior = 0
menor = 0
media = 0
cont = 0
r = ''
while r != 'N':
    n = int(input('Digite um número inteiro: '))
    r = str(input('Quer continuar? [S/N] ')).upper().strip()
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        
        if n < menor:
            menor = n
    cont += 1
    media += n
print('MEDIA: {:.2f}'.format(media/cont))
print('Maior valor digitado: {}'.format(maior))
print('Menor valor digitado: {}'.format(menor))