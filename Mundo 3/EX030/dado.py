def leia_dado(esc):
    valido = False
    while not valido:
        entrada = str(input(esc)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'ERRO: \"{entrada}\" é um Preço invalido')
        else:
            valido = True
            return float(entrada)