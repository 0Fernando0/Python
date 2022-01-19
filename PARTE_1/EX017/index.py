import math
n1 = float(input('Qual o Comprimento do Cateto Oposto? '))
n2 = float(input('Qual o Comprimento do Cateto Adjacente? '))
hipo = math.hypot(n1,n2)
#num = pow(n1,2) + pow(n2,2)
#num1 = math.sqrt(num)
#num = math.sqrt(pow(n1,2) + pow(n2,2))
print('o valor da hipotenusa é {}'.format(math.trunc(hipo)))