print('='*15)
print('NÚMEROS PRIMOS')
print('='*10)
n = int(input('digite um número: '))
cont = 0
for c in range(1,n + 1):
    if n % c == 0:
        cont += 1
        print('{}{}{}'.format('\033[33m',c,'\033[m'),end=' ')
    else:
        print('{}{}{}'.format('\033[31m',c,'\033[m'),end=' ')
print('\no número {} é divisivel {} vezes'.format(n,cont))
if cont == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')

