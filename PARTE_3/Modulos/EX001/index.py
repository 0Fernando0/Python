from moeda import dobro,aumentar,metade
num = float(input('Digite um preço: R$'))
print(f'o dobro de R${num:.2f} é R${dobro(num):.2f}')
print(f'a metade de R${num:.2f} é R${metade(num):.2f}')
print(f'aumentando 10% temos R${aumentar(num):.2f}')