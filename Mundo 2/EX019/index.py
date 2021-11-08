for c in range (1,6):
    peso = float(input('peso {}° :'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior é {}'.format(maior))
print('o menor é {}'.format(menor))