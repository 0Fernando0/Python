num = float(input('preço do produto: '))
num2 = float(input('porcentagem de desconto: '))
n1 = (num / 100) * num2
n2 = num - n1
print('o produto custa {:.2f}'.format(num))
print('o valor do desconto é {:.2f}'.format(n1))
print('o produto custará {:.2f}'.format(n2))