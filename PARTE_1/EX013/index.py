'''
script que aumenta o valor(salario) informado com base na porcentagem desejada
'''

valor = float(input('seu sálario: '))

porcentagem = float(input('seu aumento(%): '))

aumento = (valor / 100) * porcentagem

salario = valor + aumento

print(f'o seu sálario é R${valor:.2f}')
print(f'seu aumento é de R${aumento:.2f}')
print(f'ao final do mês receberá R${salario:.2f}')