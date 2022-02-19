'''
script para saber média e a situação de aluno
'''

nota_1 = float(input('primeira nota do aluno: '))
nota_2 = float(input('Segunda nota do aluno: '))

media = (nota_1 + nota_2) / 2

print('Sua media foi {}'.format(media))
if media >= 7:
    print('ALUNO APROVADO!')
elif media < 5:
    print('ALUNO REPROVADO!')
else:
    print('ALUNO EM RECUPERAÇÃO')
    