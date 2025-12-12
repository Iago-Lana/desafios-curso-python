"""
Desafio 053: Crie um programa
que leia uma frase
qualquer e diga se ela é
um palíndromo,
desconsiderando os
espaços.
"""
frase = str(input('Digite uma frase: ')).strip().replace(' ','').upper()
pd = frase[::-1]
for frase in range(1,2,-1):
    pd = frase
print('A frase {} ao contrário é {}'.format(frase,pd))
if frase == pd:
    print('A frase {} é um palíndromo.'.format(frase))
else:
    print('A frase {} não é um palíndromo.'.format(frase))
