'''
script que mostra a hipotenusa de um angulo
'''

from math import hypot,trunc

n1 = float(input('Qual o Comprimento do Cateto Oposto? '))
n2 = float(input('Qual o Comprimento do Cateto Adjacente? '))

hipo = hypot(n1,n2)

print(f'o valor da hipotenusa é {trunc(hipo)}')