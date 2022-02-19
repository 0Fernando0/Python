cor_1 = '\033[35m'
cor_2 = '\033[m'
print('-=-'*12)
print(f'{cor_1}LOJA DO FERNANDO{cor_2}')
print('-=-'*12)
valor = float(input('Valor Das Compras? '))

opcao = int(input('''
FORMAS DE PAGAMENTO
[ 1 ] à vista Dinheiro/Cheque
[ 2 ] à Vista Cartão
[ 3 ] 2x No Cartão
[ 4 ] 3x ou Mais No Cartão
SUA OPÇÃO: '''))
if opcao == 1:
    _valor = valor - ((valor / 100) * 10)
    print(f'Sua Compra Saira Por {cor_1}{_valor:.2f}{cor_2}')
elif opcao == 2:
    _valor = valor - ((valor / 100) * 5)
    print(f'Sua Compra Saira Por {cor_1}{_valor:.2f}{cor_2}')
elif opcao == 3:
    par = valor / 2
    print(f'Sua parcela saira por {cor_1}{par:.2f}{cor_2}')
    print(f'sua Compra Saira por {cor_1}{valor:.2f}{cor_2}')
elif opcao == 4:
    n = int(input('Em Quantas Vezes foi Parcelado? '))
    parcela = (valor / n) + (((valor / n)/ 100) * 20)
    _valor = valor + ((valor / 100) * 20)
    print(f'Sua parcela saira {cor_1}{parcela:.2f}{cor_2} com Juros')
    print(f'Sua compra saira Por {cor_1}{_valor:.2f}{cor_2}')
else:
    print('[ERRO]Número Invalido')
