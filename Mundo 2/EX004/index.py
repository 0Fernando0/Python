import datetime
nasc = int(input('Qual Seu Ano de nascimento? '))
atual = datetime.date.today().year
idade = atual - nasc
alistamento = nasc + 18
print('você tem {} anos'.format(idade))
if idade < 18:
    print('Faltam {} anos para você se alistar!'.format(18 - idade))
    print('você ainda deverá se apresentar no ano {}!'.format(alistamento))
elif idade == 18:
    print('Você deve se alistar Imediatamente!')
else:
    print('ja passou o tempo de alistamento!')
    print('Seu ano de alistamento foi {}'.format(alistamento))
    print('Se passou {} anos de se alistar'.format(atual - alistamento))