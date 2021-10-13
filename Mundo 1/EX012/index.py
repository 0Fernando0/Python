num = int(input('preço do produto: '))
num2 = int(input('porcentagem de desconto: '))
n1 = (num / 100) * num2
n2 = num - n1
print('o produto custa {}'.format(num))
print('o valor do desconto é {}'.format(n1))
print('o produto custará {}'.format(n2))