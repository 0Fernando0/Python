'''
script para calcular o gasto com carro alugado
usando como base os quilômetros
e também os dias que permaneceu alugado
'''

km = float(input('quantos quilômetros percorridos? '))

dias = int(input('quantos dias o veiculo permaneceu alugado? '))

preco = (dias * 60) + (km * 0.15)

print(f'você pagará R${preco:.2f}')