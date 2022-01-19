import datetime
nasc = int(input('qual o seu ano de nascimento? '))
atual = datetime.date.today().year
idade = atual - nasc
if idade <= 9:
    print('ATLETA MIRIM')
elif idade > 9 and idade <= 14:
    print('ATLETA INFANTIL')
elif idade > 14 and idade <= 19:
    print('ATLETA JUNIOR')
elif idade == 20:
    print('ATLETA SENIOR')
else:
    print('ATLETA MASTER')