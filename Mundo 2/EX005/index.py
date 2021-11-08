n1 = float(input('primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2
print('Sua media foi {}'.format(media))
if media < 5:
    print('ALUNO REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('ALUNO EM RECUPERAÇÃO')
else:
    print('ALUNO APROVADO!')