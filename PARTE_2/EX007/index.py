'''
script que infroma se é possivel formar um triangulo e que tipo de triangulo
'''
angulo = []

for c in range(1,4):
    angulo.append(float(input(f'{c}° angulo: ')))

a = angulo[0]
b = angulo[1]
c = angulo[2]

if a + b > c and c + a > b and c + b > a:
    print('PODE FORMAR UM TRIANGULO ',end='')
    if a == b == c:
        print('EQUILATERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISOCESLES')
else:
    print('NÃO É POSSIVEL FORMAR UM TRIANGULO')