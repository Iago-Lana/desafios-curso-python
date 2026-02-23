"""
Desafio 067: Faça um programa
que mostre a tabuada
de vários números, um
de cada vez, para cada
valor digitado pelo
usuário. O programa
será interrompido
quando o número
solicitado for
negativo
"""
cont = 1
while True:
    t = int(input('Quer ver a tabuada de qual número? '))
    print('='*45)
    if t < 0:
        break
    while cont <= 10:
        print(f'{t} X {cont} = {t*cont}')
        cont += 1
    cont = 1
    print('='*45)
print('Fim do programa.')
