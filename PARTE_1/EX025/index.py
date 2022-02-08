'''
pequeno script que informa 
se é possivel ou não formar um triangulo
com base nos angulos
'''


a = int(input('digite seu primeiro angulo: '))
b = int(input('digite seu segundo angulo: '))
c = int(input('digite seu terceiro angulo: '))
res = a + b
if res > c:
    print('é possivel formar um triangulo!')
else:
    print('não é possivel formar triangulo!')