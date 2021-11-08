n = int(input('escolha um numero inteiro: '))
print('''Escolha Uma Das Bases Para Conversão: 
[ 1 ] para converter para BINÁRIO
[ 2 ] para converter para OCTAL
[ 3 ] para converter para HEXADECIMAL''')
opção = int(input('sua opção: '))
if opção == 1:
    print('o número {} em binário é {}'.format(n,bin(n)[2:]))
elif opção == 2:
    print('o número {} em octal é {}'.format(n,oct(n)[2:]))
elif opção == 3:
    print('o número {} em hexadecimal é {}'.format(n,hex(n)[2:]))
else:
    print('[ERRO] Valor Invalido')