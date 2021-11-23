lista = []
while True:
    nome = str(input('Nome: ')).capitalize()
    sexo = str(input('Sexo: [M/F] ')).upper()
    idade = int(input('Idade: '))
    pergunta = str(input('Quer continuar? [S/N] ')).upper()
    if pergunta == 'S':
        continue
    elif pergunta == 'N':
        break
    else:
        print('opção invalida')
        pergunta = str(input('Quer continuar? [S/N] ')).upper()
        if pergunta == 'S':
            continue
        elif pergunta == 'N':
            break
#media = (soma/cont)