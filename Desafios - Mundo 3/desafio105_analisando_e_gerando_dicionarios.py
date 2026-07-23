"""
Faça um programa
que tenha uma função
notas() que pode
receber várias notas
de alunos e vai
retornar um dicionário
com as seguintes
informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as
docstrings da função
"""


def notas(*n, sit=False):
   """
   > Função para analisar e situação de alunos
    :param n: Uma ou mais notas dos alunos (Aceita várias)
    :param sit: Valor opcional, indicando se deve ou mostrar a situação
    :return: Dicionário com varias informações sobre a situação da turma
    """
   turma = dict()
   turma['Total'] = len(n)
   turma['Maior'] = max(n)
   turma['Menor'] = min(n)
   m = 0
   for c in n:
      m += c
   turma['Média'] = m / len(n)
   if sit:
      if turma['Média'] >= 7:
        turma['Situação'] = 'BOA'
      elif turma['Média'] >=5:
         turma['Situação'] = 'RAZOAVEL'
      else:
         turma['Situação'] = 'RUIM'
   return turma


resp = notas(5,6,9,1,3, sit=True)
print(resp)
help(notas)
