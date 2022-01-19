vcasa = float(input('Qual o Valor da casa? R$'))
salario = float(input('Qual o Seu salario mensal? R$'))
anos = int(input('Em Quantos Anos você vai pagar? '))
parsal = ((salario/100) * 30)
parcelas = vcasa / (anos * 12)
if parcelas <= parsal:
    print('APROVADO,por {} Anos você pagara de parcelas de sua casa R${:.2f}'.format(anos,parcelas))
else:
    print('Infelizmente Seu Emprestimo foi Negado!')