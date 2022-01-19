from typing import Reversible


contaidade = contamulher = contahomem = 0
while True:
    print('='*20,'\nCADASTRE UMA PESSOA\n','='*20)
    idade = int(input('idade: '))
    if idade > 18:
        contaidade += 1
    sexo = str(input('sexo: [M/F] ')).upper()
    if sexo == 'M':
        contahomem += 1
    if sexo == 'F' and idade < 20:
        contamulher += 1
    print('='*20)
    escolha = str(input('Quer Continuar? [S/N] ')).upper()
    if escolha == 'S':
        reversed
    elif escolha == 'N':
        print(f'{contaidade} pessoas tem mais de 18 anos')
        print(f'{contahomem} homens foram cadastrados')
        print(f'{contamulher} mulheres tem menos de 20 anos')
        break
    else:
        print('[ERRO] OPÇÃO INVALIDA')
        