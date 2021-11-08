from random import randint
print('='*40)
print('           JOGO DE ADIVINHAÇÃO')
print('='*40)
print('''adivinhe o número que estou pensando...
uma dica é de 1 até 100''')
maquina = randint(1,100)
while True:
    usuario = int(input('Sua escolha? '))
    if usuario == maquina:
        print('VOCÊ ACERTOU PARABENS!!!')
        break
    elif usuario > maquina:
        print('MENOS...')
    elif usuario < maquina:
        print('MAIS...')
print('OBRIGADO POR PARTICIPAR')
