km = float(input('quantos quilômetros percorridos? '))
dias = int(input('quantos dias o veiculo permaneceu alugado? '))
preco = (dias * 60) + (km * 0.15)
#preco = dias * 60 
#preco2 = km * 0.15
#res = preco + preco2
print('você pagará R${:.2f}'.format(preco))