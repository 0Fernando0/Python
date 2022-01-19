roxo = '\033[35m'
fim = '\033[m'
print('-=-'*12)
print('{}LOJA DO FERNANDO{}'.format(roxo,fim))
print('-=-'*12)
valor = float(input('Valor Das Compras? '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista Dinheiro/Cheque
[ 2 ] à Vista Cartão
[ 3 ] 2x No Cartão
[ 4 ] 3x ou Mais No Cartão''')
opcao = int(input('QUAL A SUA OPÇÃO: '))
if opcao == 1:
    print('Sua Compra Saira Por {}{:.2f}{}'.format(roxo,valor - ((valor / 100) * 10),fim))
elif opcao == 2:
    print('Sua Compra Saira Por {}{:.2f}{}'.format(roxo,valor - ((valor / 100) * 5),fim))
elif opcao == 3:
    par = valor / 2
    print('Sua parcela saira por {}{:.2f}{}'.format(roxo,par,fim))
    print('sua Compra Saira por {}{:.2f}{}'.format(roxo,valor,fim))
elif opcao == 4:
    n = int(input('Em Quantas Vezes foi Parcelado? '))
    parcela = (valor / n) + (((valor / n)/ 100) * 20)
    print('Sua parcela saira {}{:.2f}{} com Juros'.format(roxo,parcela,fim))
    print('Sua compra saira Por {}{:.2f}{}'.format(roxo,valor + ((valor / 100) * 20),fim))

else:
    print('[ERRO]Número Invalido')
