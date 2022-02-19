print('='*20)
print('BANCO BORGES'.center(20))
print('='*20)
valor = int(input('Que Valor Você Quer Sacar: R$'))
total = valor
nota = 50
cont = 0
while True:
    if total >= nota:
        total -= nota
        cont += 1
    else:
        print(f'total de {cont} cedulas de {nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        cont = 0
        if total == 0:
            break
