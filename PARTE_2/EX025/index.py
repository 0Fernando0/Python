print('='*10,'10 Primeiros termos da P.A','='*10)
termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
decimo = termo + (11 - 1) * razão
while termo != decimo:
    termo += razão
    print(termo,end=' ')