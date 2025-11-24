"""
Desafio 043: Desenvolva uma lógica
que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso

- Entre 18.5 e 25: Peso Ideal

- 25 até 30: Sobrepeso

- 30 até 40: Obesidade

- Acima de 40: Obesidade morbida
"""
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso/altura**2
if imc < 18.5:
    print('Com {:.1f} de imc você está ABAIXO DO PESO.'.format(imc))
elif 18.5 <= imc < 25:
    print('Com {:.1f} de imc você está com o PESO IDEAL.'.format(imc))
elif 25 <= imc < 30:
    print('Com {:.1f} de imc você está com SOBREPESO'.format(imc))    
elif 30 <= imc < 40:
    print('Com {:.1f} de imc você está com OBESIDADE'.format(imc))
elif imc >= 40:
    print('Com {:.1f} de imc você está com OBESIDADE MORBIDA.'.format(imc))
     