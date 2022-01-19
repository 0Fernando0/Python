from moeda import resumo
valor = float(input('Digite um valor: '))
adicional = float(input('Quantos porcentos de adicional: '))
redução = float(input('Quantos porcentos de redução: '))
res = resumo(valor,adicional,redução)
print(res)