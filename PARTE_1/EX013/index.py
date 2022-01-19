num = float(input('seu sálario: '))
num2 = float(input('seu aumento em porcentagem: '))
n1 = (num / 100) * num2
n2 = num + n1
print('o seu sálario é R${:.2f}'.format(num))
print('seu aumento é de R${:.2f}'.format(n1))
print('ao final do mês receberá R${:.2f}'.format(n2))