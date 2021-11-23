from _typeshed import StrPath


def fatorial(num):
    n = 1
    cont = 0
    print(num,end=' ')
    for c in range(num,0,-1):
        n *= c
        cont += 1
        if cont >= 2:
            print(f'x {c}',end=' ')
    print(f'= {n}')
fatorial(5)