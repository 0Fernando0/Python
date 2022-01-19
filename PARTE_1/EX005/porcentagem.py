n1 = float(input('Qual a Porcentagem? '))
n2 = float(input('Qual o Valor? '))
n3 = (n2 / 100) * n1
n4 = n2 - n3
print('{}% de {} é {:.2f}'.format(n1,n2,n3))
print('sobrará {:.2f}'.format(n4))