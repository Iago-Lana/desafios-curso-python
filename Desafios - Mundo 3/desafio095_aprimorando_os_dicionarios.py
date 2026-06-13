"""
Desafio 095: Aprimore o desafio
093 para que ele
funcione com vários
jogadores, incluindo
um sistema de
visualização do
aproveitamento de
cada jogador.
"""
jogador = dict()
dados = list()
while True:
    gols = list()
    tot = 0
    jogador['nome'] = str(input('Nome: '))
    jogador['partida'] = int(input('Quantas partidas ele jogou? '))
    for c in range(jogador['partida']):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
        jogador['gols'] = gols
    for t in gols:
        tot += t
    jogador['total'] = tot
    dados.append(jogador.copy())
    r = str(input('Deseja continuar? [S/N] ')).upper()
    if r in 'N':
        break
print('='*60)
print(f'{'cod name':<20} {'gols':<20} {'total':<20}')
print('='*60)
for c, n in enumerate(dados):
    print(f'{c:<3} {n['nome']:<16} {str(n['gols']):<20} {n['total']:<20}')
print('='*60)
while True:
    r = int(input('Deseja ver os dados de qual jogador? [999 para encerrar] '))
    if r == 999:
        break
    print('='*60)
    for j, g in enumerate(dados):
        if r == j:
            print(f'-- Levantamento do jogador {g['nome']}')
            for p, t in enumerate(g['gols']):
                print(f'{'No Jogo':>10} {p} fez {t} gols.')
            print('*60')
print('<< VOLTE SEMPRE >>')
