menor = maior = cont = soma = 0
while True:
    numero = int(input('digite um número: '))
    print('Quer adicionar mais algum número? [S] ou [N]')
    opcao = str(input('sua escolha: ')).upper()
    cont += 1
    soma += numero
    if opcao == 'N':
        if cont == 1:
            maior = menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero
        media = soma / cont
        print('o valor {} é maior e o valor {} é o menor'.format(maior,menor))
        print('a media entre eles foi {:.2f}'.format(media))
        print('PROGRAMA ENCERRADO...')
        break
    elif opcao == 'S':
        continue
    else:
        print('[ERRO]')
        break