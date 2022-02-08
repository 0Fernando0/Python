'''
script que acrescenta
10% se o salario for maior que R$1250,00
15% se o salario for menor que R$1250,00
'''

salario = float(input('Qual o seu salario? R$'))

aumento_1 = ((salario/100) * 10) + salario
aumento_2 = ((salario/100) * 15) + salario

if salario > 1250:
    print(f'com seu aumento de 10% você vai receber R${aumento_1:.2f}')
else:
    print(f'com seu aumento de 15% você vai receber R${aumento_2:.2f}')