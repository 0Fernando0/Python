'''
script para verificar quanto tempo falta para a pessoa se alistar 
'''

from datetime import datetime

nascimento = int(input('Qual Seu Ano de nascimento? '))
ano_atual = datetime.now().year
idade = ano_atual - nascimento
alistamento = nascimento + 18

print(f'você tem {idade} anos')

if idade < 18:
    print(f'Faltam {18 - idade} anos para você se alistar!')
    print(f'você ainda deverá se apresentar no ano {alistamento}!')
elif idade == 18:
    print(f'Você deve se alistar Imediatamente!')
else:
    print(f'ja passou o tempo de alistamento!')
    print(f'Seu ano de alistamento foi {alistamento}'.format(alistamento))
    print(f'Se passou {ano_atual - alistamento} anos de se alistar')