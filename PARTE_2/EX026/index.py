print('='*10,'10 Primeiros termos da P.A','='*10)
termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
decimo = termo + (11 - 1) * razão
while termo != decimo:
    termo += razão
    print(termo,end=' ')
termo2 = termo
print('''\nDeseja Ver Mais alguns Termos?
[ 1 ] para Sim
[ 0 ] para Não''')
opção = int(input('Sua escolha: '))
while opção != 0:
    if opção == 1:
        print('\nQuantos Termos A mais? ')
        opc = int(input('Sua Escolha: '))
        adicionar = termo2 + opc * razão
        if opc == 0:
            break
        while termo2 != adicionar:
            termo2 += razão
            print(termo2,end=' ')         
    else:
        print('[ERRO] Opção Invalida')
print('PROGRAMA ENCERRADO...')
exit


    


