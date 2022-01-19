lista = []
print('DIGITE (999) PARA ENCERRA PROGRAMA')
while True:
    n = int(input('digite uma número: '))
    if n == 999:
        print(f'os valores adicionados foram: ',end='')
        for c in sorted(lista):
            print(c,end=' ')
        break
    if n in lista:
        print('número duplicado,por favor digite outro! ')
    else:
        print('valor adicionado com sucesso!')
        #lista += [n]
        lista.append(n)