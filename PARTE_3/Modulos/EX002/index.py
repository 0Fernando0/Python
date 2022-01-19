from moeda import metade,dobro,moeda,aumentar
num = float(input('Digite um preço: R$'))
print(f'o dobro de {moeda(num)} é {moeda(dobro(num))}')
print(f'a metade de {moeda(num)} é {moeda(metade(num))}')
print(f'aumentando 10% temos {moeda(aumentar(num))}')