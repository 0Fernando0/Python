soma = 0
cont = 0
while True:
    n = int(input('Digite um valor [999 para encerrar programa]: '))
    soma += n
    cont += 1
    if n == 999:
        print('foram contabilizados {} vezes'.format(cont - 1))
        print('a soma foi {}'.format(soma - 999))
        print('Programa Encerrado...')
        break

