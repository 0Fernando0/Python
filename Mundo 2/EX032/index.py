from random import randint
while True:
    n = int(input('Escolhe um número: '))
    r = str(input('Impar ou Par: [I] ou [P] ')).upper()
    computador = randint(1,n)
    if r == 'I':
        if (n + computador) % 2 == 1: #impar
            print('VOCÊ GANHOU')
        elif (n + computador) % 2 == 0:
            print('VOCÊ PERDEU')
            break
    if r == 'P':
        if (n + computador) % 2 == 0: #par
            print('VOCÊ GANHOU')
        elif (n + computador) % 2 == 1:
            print('VOCÊ PERDEU')
            break
    print(f'o computador pensou em {computador}')
    
