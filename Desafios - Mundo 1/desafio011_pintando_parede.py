"""
Desafio 011: Faça um programa que leia largura e a altura de uma parede em metros, calcule  sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

"""
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
print('Sua parede tem uma dimensão de {}x{} e uma área de {}m²'.format(largura,altura, largura*altura))
print('Para pintar essa parede você precisa de {}L de tinta.'.format((largura*altura)/2))