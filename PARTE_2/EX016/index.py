print('='*10)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('='*10)
n = int(input('primeiro termo: '))
razão = int(input('Razão: '))
oitavo = n + (11 - 1) * razão
soma = 0
cont = 0
for c in range(n,oitavo,razão):
    cont += 1
    print(c,end=' ')
    if cont == 2 or cont == 4 or cont == 8:
        soma += c
print('\na soma é {}'.format(soma))