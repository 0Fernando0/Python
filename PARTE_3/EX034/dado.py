def leia_int(n):
    while True:
        try:
            nu = int(input(n))
        except(ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return nu
def leia_float(n):
    while True:
        try:
            nu = float(input(n))
        except(ValueError,TypeError):
            print('ERRO: por favor, digite um número real valido')
        else:
            return nu

def leia_dado(esc):
    valido = False
    while not valido:
        entrada = str(input(esc)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: \"{entrada}\" é um Preço invalido')
        else:
            valido = True
            return float(entrada)
