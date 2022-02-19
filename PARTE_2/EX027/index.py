soma = cont = 0
while True:
    numero = int(input('Digite um valor [999 para encerrar programa]: '))
    soma += numero
    cont += 1
    if numero == 999:
        print('foram contabilizados {} vezes'.format(cont - 1))
        print('a soma foi {}'.format(soma - 999))
        print('Programa Encerrado...')
        break

