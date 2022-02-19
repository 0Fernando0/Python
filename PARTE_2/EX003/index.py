'''
script para ver o maior e o menor número informado
'''

lista = []
for c in range(2):
    lista.append(int(input('digite um número: ')))

if lista[0] > lista[1]:
    print(f'o número {lista[0]} é maior')
elif lista[1] > lista[0]:
    print(f'o número {lista[1]} é maior')
else:
    print('não existe valor maior, ambos são iguais') 