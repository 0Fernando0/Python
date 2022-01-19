s = 0
cont = 0
for c in range(1,7):
    n = int(input('digite um numero inteiro: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('a soma dos números pares foi {}{}{}'.format('\033[33m',s,'\033[m'))
print('você digitou {} números pares'.format(cont))