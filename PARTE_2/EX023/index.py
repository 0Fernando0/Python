while True:   
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR 
    [ 4 ] NOVOS NÚMERO
    [ 5 ] ENCERRAR PROGRAMA
    ''')
    opcao = int(input('Sua Opção: '))
    if opcao == 1:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        n3 = n1 + n2
        print('A Soma de {} com {} é {}'.format(n1,n2,n3))
    elif opcao == 2:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        n3 = n1 * n2
        print('A Multiplicação de {} com {} é {}'.format(n1,n2,n3))
    elif opcao == 5:
        print('FIM DO PROGRAMA')
        break
    elif opcao == 3:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        if n1 > n2:
            print('o {} é maior que {}'.format(n1,n2))
        elif n2 > n1:
            print('o {} é maior que {}'.format(n2,n1))
        else:
            print('Não existe maior, eles são iguais')
    elif opcao == 4:
        import random
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))
        novonum = random.randint(1,n1)
        novonum2 = random.randint(1,n2)
        print('os novos números são {} e {}'.format(novonum,novonum2))
    else:
        print('[ERRO] Valor invalido!')