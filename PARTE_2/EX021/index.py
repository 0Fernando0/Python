while True:
    opcao = str(input('''
    Qual O Seu Sexo [ M ] [ F ]
    Sua Opção: ''')).upper()
    if opcao == 'M':
        print('O Seu sexo é Masculino')
        print('Para Sair Digite: exit')
    elif opcao == 'F':
        print('O Seu sexo é Feminino')
        print('Para Sair Digite: exit')
    elif opcao == 'EXIT':
        print('PROGRAMA ENCERRADO...')
        break
    else:
        print('''
        [ERRO] Valor Invalido
        Por Favor Digite Somente (M) ou (F)
        Para Sair Digite: exit
        ''')   
        
    