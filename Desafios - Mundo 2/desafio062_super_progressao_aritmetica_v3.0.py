"""
Desafio 062: Melhore o desafio
061, perguntando para
o usuário se ele quer
mostrar mais alguns termos. O programa
encerra quando ele
disser que quer
mostrar 0 termos.
"""
tottermos = 0
t = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = 1
c = 10
p = 0
while c != 0:
    c += p
    while d <= c:
        print('{} ->'.format(t),end=' ')
        t += r
        d += 1
        tottermos += 1
    print('PAUSA')
    p = int(input('Mais quantos termos você quer mostrar? '))
    if p == 0:
        c = p
print('Progressao finalizada com {} termos mostrados.'.format(tottermos))
