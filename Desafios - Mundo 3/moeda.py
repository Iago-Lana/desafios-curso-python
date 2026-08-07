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
