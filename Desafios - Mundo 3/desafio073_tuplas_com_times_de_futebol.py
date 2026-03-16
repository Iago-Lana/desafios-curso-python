"""
Desafio 073: Crie uma Tupla
preenchida com os 20
primeiros colocados
da tabela do
campeonato Brasileiro
de Futebol, na ordem
de colocação. Depois
mostre:

A) Apenas os 5
primeiros colocados.

B) Os últimos 4
colocados da tabela.

C) Uma lista com os
times em ordem
alfabética.

D) Em que posição na
tabela está o time da
Chapecoense.
"""
times = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Bragantino', 'Flamengo', 'Coritiba', 'Corinthians', 'Grêmio',
'Athletico-PR', 'EC Vitória', 'Vasco da Gama', 'Mirassol',
'Santos', 'Chapecoense', 'Athlético-MG', 'Botafogo', 'Remo', 'Internacional', 'Cruzeiro' )
print(f'Lista com os times do Brasileirão: {times}')
print('='*139)
print(f'\nOs 5 primeiros colocados são {times[:5]}')
print(f'\nOs 4 últimos colocados são: {times[-4:]}')
print(f'\nLista dos times em ordem afabética: {sorted(times)}')
print(f'\nA Chapecoense está na {times.index('Chapecoense')}° Posição')
print('='*139)
