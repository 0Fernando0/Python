m = 0
totmulher = 0
for c in range(1,5):
    print('-'*5,end=' ')
    print('{}ª PESSOA'.format(c),end=' ')
    print('-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    m += idade
    media = m / 4
    if c == 1 and sexo in 'M':
        maioridadehom = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehom:
        maioridadehom = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher += 1
print('a media de idade do grupo foi de {}'.format(media))
print('O homem mas velho tem {} anos e tem o nome de {}'.format(maioridadehom,nomevelho))
print('{} mulheres tem menos de 20 anos'.format(totmulher))
