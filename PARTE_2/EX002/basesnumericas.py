'''
script que faz a conversão de um número para binario,octal ou hexadecimal
'''

numero = int(input('escolha um numero inteiro: '))
print('''
Escolha Uma Das Bases Para Conversão: 
[ 1 ] para converter para BINÁRIO
[ 2 ] para converter para OCTAL
[ 3 ] para converter para HEXADECIMAL
''')

opção = int(input('sua opção: '))

if opção == 1:
    print(f'o número {numero} em binário é {bin(numero)}')
elif opção == 2:
    print(f'o número {numero} em octal é {bin(numero)}')
elif opção == 3:
    print(f'o número {numero} em hexadecimal é {bin(numero)}')
else:
    print('[ERRO] Valor Invalido')