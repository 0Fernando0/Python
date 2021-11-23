lista = []# lista = list()
par = []# par = list()
impar = []# impar = list()
while True:
    n = int(input('digite um número: '))
    if n == 999:
        print(f'os números digitados foram {lista}')
        print(f'os numeros pares foram {par}')
        print(f'os numeros pares foram {impar}')
        break
    lista.append(n)
    if n % 2 == 0:
        par.append(n) 
    else:
        impar.append(n)      