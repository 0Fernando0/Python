real = float(input('Dinheiro Atual na Carteira? R$'))
dolar = real / 5.51
euro = real / 6.37
libra = real / 7.53
franco = real / 5.97
print('você tem R${:.2f}'.format(real))
print('pode comprar até US${:.2f}'.format(dolar))
print('pode comprar até €{:.2f}'.format(euro))
print('pode comprar até £{:.2f}'.format(libra))
print('pode comprar até CHF{:.2f}'.format(franco))