'''
script reduz o valor do um produto com base no desconto(%)
'''

produto = float(input('preço do produto: '))

desconto = float(input('porcentagem de desconto: '))

novo_preço = produto - ((produto / 100) * desconto)

print(f'o produto custa {produto:.2f}')
print(f'o valor do desconto é {desconto:.2f}')
print(f'o produto custará {novo_preço:.2f}')