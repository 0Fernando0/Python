print('='*20)
print('LISTA DE COMPRAS')
print('='*20)
soma = contavalor = cont = 0
while True:
    produto = str(input('Nome Do Produto: '))
    valor = float(input('Preço: R$'))
    cont += 1
    soma += valor
    if valor > 1000:
        contavalor += 1
    if cont == 1 or valor < menor:
        menor = valor
        barato = produto
    resposta = str(input('Deseja Continuar? [S/N] ')).upper()
    if resposta == 'S':
        continue
    elif resposta == 'N':
        print(f'O Total da Compra Foi R${soma:.2f}')
        if contavalor:
            print(f'{contavalor} Produtos Custaram Mais de R$1000')
        print(f'o Produto mais barato foi {barato}  que custa R${menor:.2f}')
        break