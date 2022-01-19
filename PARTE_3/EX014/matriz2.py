matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = somac = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'digite um número [{l}.{c}] : '))
        if l == 1:
            maior = max([matriz[l][c]])
        if c == 2:
            somac += matriz[l][c]
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
print('='*40)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('='*40)
print(f'a soma dos pares é {soma}')
print(f'a soma dos valores da terceira coluna é {somac}')
print(f'o maior valor da segunda linha é {maior}')
