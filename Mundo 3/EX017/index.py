n = str(input('Nome Do Aluno: ')).capitalize()
media = float(input('Qual A Media do Aluno: '))
lista = {'Nome':n,'Média':media}
print('='*40)
if media >= 6:
    lista['Situação'] = 'Aprovado'
else:
    lista['Situação'] = 'Reprovado'
for n,r in lista.items():
    print(f'- {n} é igual a {r}')