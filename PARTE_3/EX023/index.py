for c in range(1,11,1):
    print(f'{c}',end=' ')
print('FIM')
for c in range(10,-1,-2):
    print(f'{c}',end=' ')
print('FIM')
print('agora é sua vez de personalizar a contagem!')
us = int(input('inicio: '))
us2 = int(input('fim: '))
us3 = int(input('intervalo: '))
def contador(us,us2,us3):
    if us > us2 and us3 == 0:
        for c in range(us,us2-1,-1):
            print(f'{c}',end=' ')
        print('FIM')
    else:
        if us3 == 0:
            for c in range(us,us2+1,1):
                print(f'{c}',end=' ')
            print('FIM')
        elif us > us2:
            for c in range(us,us2-1,-us3):
                print(f'{c}',end=' ')
            print('FIM')
        else:
            for c in range(us,us2+1,us3):
                print(f'{c}',end=' ')
            print('FIM')
contador(us,us2,us3)