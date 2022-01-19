n = int(input('digite um número: ')),int(input('digite outro número: ')),int(input('digite mais um número: ')),int(input('digite o ultimo número: '))
print('Os Números Foram:',end= ' ')
for c in n:
    print(c,end=' ')
print(f'\no número 9 aparece {n.count(9)} vezes')
if 3 in n:
    print(f'o número 3 se encontra na {n.index(3)+1}ª posição')
else:
    print('o número 3 não se encontra em nenhuma posição')
print(f'Os números pares são: ',end='')
for c in n:
    if c % 2 == 0:
        print(c,end=' ')