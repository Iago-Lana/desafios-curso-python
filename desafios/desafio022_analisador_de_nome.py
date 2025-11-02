"""
Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre:

° O nome com todas as letras maiúsculas
° O nome com todos minúsculas
° Quantas letras ao todo (sem considerar espaços).
° Quantas letras tem o primeiro nome.

"""
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas:',nome.upper())
print('Seu nome com todas as letras minúsculas:',nome.lower())
print('Seu nome tem ao todo: {} letras'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))