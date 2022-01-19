from random import randint
lista = []
while True:
    p = int(input('Quantos Palpites você quer? '))
    for c in range(1,p+1):
        for c in range(1,7):
            lista = [randint(1,60)]
            print(f'{lista}',end='')
        print()
    res = str(input('Você deseja outro palpite? [S/N] ')).upper()
    if res == 'S':
        continue
    if res == 'N':
        print('BOA SORTE!')
        break
