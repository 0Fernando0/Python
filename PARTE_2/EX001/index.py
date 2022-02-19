'''
script de aprovação de financiamento de casa
'''

valor_casa = float(input('Qual o Valor da casa? R$'))
salario = float(input('Qual o Seu salario mensal? R$'))
tempo = int(input('Em Quantos Anos você vai pagar? '))

parcela_salario = ((salario/100) * 30)
parcela_casa = valor_casa / (tempo * 12)

if parcela_casa <= parcela_salario:
    print(f'APROVADO,por {tempo} Anos você pagara de parcelas de sua casa R${parcela_casa:.2f}')
else:
    print('Infelizmente Seu Emprestimo foi Negado!')