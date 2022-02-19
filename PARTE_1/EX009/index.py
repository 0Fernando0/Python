'''

um tabuada simples

'''

num = int(input('digite um número para ver sua tabuada: '))

print('=' * 11)
for c in range(1,11):
    print(f'{num} x {c:2} = {num*c:2}')

print('=' * 11)