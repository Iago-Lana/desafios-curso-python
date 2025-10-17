"""
Desafio 07: Escreva um programa que leia um valor metros e o exiba convertido em centimetros e milímetros.

"""
m = float(input('Quantos metros? '))
print(m,'(m) convertido para centimetros é igual a {} cm \ne convertido para milímetros é igual a {} mm'.format(m*100, m*1000))