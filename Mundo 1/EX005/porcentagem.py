n1 = int(input('Qual a Porcentagem? '))
n2 = int(input('Qual o Valor? '))
n3 = (n2 / 100) * n1
n4 = n2 - n3
print('{}% de {} é {}'.format(n1,n2,n3))
print('sobrará {}'.format(n4))