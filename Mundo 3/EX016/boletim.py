ficha = list()
while True:
    nome = str(input('Nome do aluno: ')).capitalize()
    n1 = float(input('1ª no aluno: '))
    n2 = float(input('2ª no aluno: '))
    media = (n1 + n2) / 2
    ficha.append([nome,[n1,n2],media])
    res = str(input('Deseja Continuar? [S/N] ')).upper()
    if 'Ss' in res:
        continue
    elif res == 'N':
        break
print(f'{ficha}')