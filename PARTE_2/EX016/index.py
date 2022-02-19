print('='*10)
print('10 PRIMEIROS TERMOS DE UMA P.A')
print('='*10)

primeiro = int(input('primeiro termo: '))
razão = int(input('Razão: '))
oitavo = primeiro + (11 - 1) * razão
soma = cont = 0

for c in range(primeiro,oitavo,razão):
    cont += 1
    print(c,end=' ')
    if cont == 2 or cont == 4 or cont == 8:
        soma += c
print('\na soma é {}'.format(soma))