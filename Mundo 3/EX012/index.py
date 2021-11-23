lista = [[],[]]
for c in range(1,8):
    n = int(input(f'digite o {c}° número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'os valores pares são {sorted(lista[0])}')
print(f'os valores impares são {sorted(lista[1])}')
        