fatorial = 1
while True:
    print('''
    [ 1 ] PARA FATORIAL
    [ 2 ] PARA SAIR
     ''')
    opcao = int(input('Sua Escolha: '))
    if opcao == 1:
        n = int(input('Número: '))
        print('{}! = {} x {}'.format(n,n,n-1),end= ' ')
        for c in range(n,0,-1):
            fatorial *= c
            if c != n - 1 and c != n:
                print('x {}'.format(c),end= ' ')
        print('= {}'.format(fatorial))
    elif opcao == 2:
        print('FIM DO PROGRAMA')
        break
    else:
        print('[ERRO] Número Invalido')