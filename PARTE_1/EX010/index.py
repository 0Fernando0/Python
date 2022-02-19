'''
script que aprensenta  o quanto você pode comprar com base na sua quantia atual
'''

real = float(input('Dinheiro Atual na Carteira? R$'))

dolar = real / 5.51
euro = real / 6.37
libra = real / 7.53
franco = real / 5.97

print(f'você tem R${real:.2f}')
print(f'pode comprar até US${dolar:.2f}')
print(f'pode comprar até €{euro:.2f}')
print(f'pode comprar até £{libra:.2f}')
print(f'pode comprar até CHF{franco:.2f}')