def leiadinheiro(n):
    while True:
        v = str(input(n)).strip()
        if v.isnumeric():
            return float(v)
        elif ',' in v or '.' in v:
            return float(v.replace(',','.'))
        else:
            print(f'\033[31mERRO: "{v}" não é um valor válido.\033[0m')