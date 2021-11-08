print('='*20)
print('BANCO BORGES')
print('='*20)
valor = int(input('Que Valor Você Quer Sacar: R$'))
total = valor
ced = 50
cont = 0
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        print(f'total de {cont} cedulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        cont = 0
        if total == 0:
            break
