num = int(input('seu sálario: '))
num2 = int(input('seu aumento em porcentagem: '))
n1 = (num / 100) * num2
n2 = num + n1
print('o seu sálario é R${}'.format(num))
print('seu aumento é de R${}'.format(n1))
print('ao final do mês receberá R${}'.format(n2))