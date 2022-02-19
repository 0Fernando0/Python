mulher_menor = maior = 0

for c in range(1,5):
    print('-'*c,end=' ')
    print('{}ª PESSOA'.format(c),end=' ')
    print('-'*c)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    maior += idade
    media = maior / 4
    if c == 1 and 'M' in sexo:
        idade_velho = idade
        nome_velho = nome
    if 'M' in sexo and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if 'F' in sexo and idade < 20:
        mulher_menor += 1

print(f'a media de idade do grupo foi de {media}')
print(f'O homem mas velho tem {idade_velho} anos e tem o nome de {nome_velho}')

if mulher_menor:
    print(f'{mulher_menor} mulheres tem menos de 20 anos')
else:
    print('nenhuma mulher tem menos de 20 anos')
