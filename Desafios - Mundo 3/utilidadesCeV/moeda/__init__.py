def aumentar(n, p, f=False):
    p = p / 100 * n
    if f:
        return moeda(n + p)
    return n + p


def diminuir(n, p, f=False):
    p = p / 100 * n
    if f:
        return moeda(n - p)
    return n - p


def dobro(n, f=False):
    if f:
        return moeda(n * 2)
    return n * 2


def metade(n, f=False):
    if f:
        return moeda(n / 2)
    return n / 2


def moeda(n):
    n = f'R${n:.2f}'.replace('.',',')
    return n


def resumo(n, a, d):
    print('='*35)
    print(f'{'RESUMO DO VALOR':>24}')
    print('='*35)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n,a ,True)}')
    print(f'{d}% de redução: \t{diminuir(n,d ,True)}')
    print('='*35)