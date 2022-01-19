lista = []
#maior = []
#menor = []
for c in range(0,5):
    n = int(input(f'digite um valor para a posição {c}: '))
    lista += [n]
print(f'os valores digitados foram {lista}')
print(f'o maior valor foi {max(lista)} na posição: ',end=' ')
for i,v in enumerate(lista):
    if v == max(lista) :
        print(f'{i}...',end='')
print(f'\no menor valor foi {min(lista)} na posição: ',end=' ')
for i,v in enumerate(lista):
    if v == min(lista) :
        print(f'{i}...',end='')