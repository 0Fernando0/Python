from datetime import date, datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('ANO DE NASCIMENTO: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de contratação: '))
    dados['salário'] = float(input('salário: R$'))
    dados['aposentadoria'] = (dados['contratação'] + 35) - datetime.now().year
for v,r in dados.items():
    print(f'- {v} é igual a {r}')