'''
script para mostrar o número inteiro
'''

from math import trunc

num = float(input('digite um número: '))

inteiro = trunc(num)

print(f'o número {num} tem a parte inteira {inteiro}')