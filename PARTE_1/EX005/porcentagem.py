'''
script de desconto de valor
'''

valor = float(input('Qual o Valor? '))
porcentagem = float(input('Qual a Porcentagem? '))

redução = (valor / 100) * porcentagem
valor_final = valor - redução

print(f'{porcentagem}% de {valor} é {redução:.2f}')
print(f'sobrará {valor_final:.2f}')