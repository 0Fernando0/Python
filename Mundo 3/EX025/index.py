from random import randint
from time import sleep
def sortear(n):
    print(f'os 5 numeros sorteados foram',end=' ')
    c = 0
    while c != n:
        c += 1
        numeros.append(randint(1,9))
    for c in numeros:
        print(c,end=' ',flush=True)
        sleep(0.2)
        
def somarPar():
    n = 0
    for c in numeros:
        if c % 2 == 0:
            n += c
    print(f'\na soma dos números pares sorteados é {n}')
numeros = []
print(f'a foi {numeros} numeros')
sortear(5)
somarPar()