def mostrarmenu():
    print('='*50)
    print('MENU PRINCIPAL'.center(48))
    print('='*50)
    print('''1 - \033[36mVer pessoas cadastradas\033[0m
2 - \033[36mCadastrar nova pessoa\033[0m
3 - \033[36mSair\033[0m''')
    print('='*50)


def mostrarcadastro():
    print('PESSOAS CADASTRADAS'.center(48))
    print('='*50)
    with open('cadastro.txt', 'r') as arquivo:
        for c in arquivo:
            c = c.replace('\n', '')
            dado = c.split(';')
            print(f'{dado[0]:<30}{dado[1]:>10} Anos')


def cadastro():
    print('NOVO CADASTRO'.center(48))
    print('='*50)
    nome = str(input('Nome: ')).title()
    while True:
        try:
            idade = int(input('Idade: '))
        except ValueError:
            print('\033[31mERRO: Digite um número inteiro\033[0m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            break
    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(f'{nome};{idade}\n')
