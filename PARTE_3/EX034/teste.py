from dado import leia_int

def linha(tam = 42):
    return '='* tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('Menu Pricipal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leia_int('Sua Opção: ')
    return opc
