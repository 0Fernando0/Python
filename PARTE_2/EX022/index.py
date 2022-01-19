import random
numeros = random.randint(0,10)
tentativas = 0
print('='* 10,'Jogo da adivinhação','='* 10)
print('Em Que numero estou pensando???')
print('DICA(o número pode se de 0 até 10)')
while True:
    opcao = int(input('Sua Escolha: '))
    if opcao < numeros:
        tentativas += 1
        print('Mais...Tente novamente!')
    elif opcao > numeros:
        tentativas += 1
        print('Menos...Tente novamente!')
    else:
        print('Você acertou!!!, Eu pensei no {}'.format(numeros))
        print('você tentou {} vez(es)'.format(tentativas + 1))
        break
