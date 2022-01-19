a1 = float(input('digite o primeiro angulo: '))
a2 = float(input('digite o segundo angulo: '))
a3 = float(input('digite o terceiro angulo: '))
if a1 + a2 > a3 and a3 + a1 > a2 and a3 + a2 > a1:
    print('PODE FORMAR UM TRIANGULO ',end='')
    if a1 == a2 == a3:
        print('EQUILATERO')
    elif a1 != a2 != a3 != a1:
        print('ESCALENO')
    else:
        print('ISOCESLES')
else:
    print('NÃO É POSSIVEL FORMAR UM TRIANGULO')