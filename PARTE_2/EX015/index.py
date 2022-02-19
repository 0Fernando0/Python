cont = soma = 0

for c in range(1,7):
    numero = int(input(f'o {c}° numero: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1

print(f'a soma dos números pares foi','\033[33m',soma,'\033[m')
print(f'você digitou {cont} números pares')