import random
import time
itens = ('PEDRA','PAPEL','TESOURA')
print('-=-'*10)
print('JOGO DO PEDRA,PAPEL E TESOURA!')
print('-=-'*10)

jogador = int(input('''
suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
Sua Jogada: '''))
computador = random.randint(0,2)

if computador == 2:
    if jogador == 0:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!')
        print('Você escolheu {}'.format(itens[jogador]))
        print('Eu Escolhi {}'.format(itens[computador]))
        print('VOCÊ VENCEU')
    elif jogador == 1:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!')
        print('Você escolheu {}'.format(itens[jogador]))
        print('Eu Escolhi {}'.format(itens[computador]))
        print('EU GANHEI')
    elif jogador == 2:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!')
        print('Você escolheu {}'.format(itens[jogador]))
        print('Eu Escolhi {}'.format(itens[computador]))
        print('DEU EMPATE')    
elif computador == 0:
    if jogador == 0:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!')
        print('Você escolheu {}'.format(itens[jogador]))
        print('Eu Escolhi {}'.format(itens[computador]))
        print('DEU EMPATE')
    elif jogador == 1:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!')
        print('Você escolheu {}'.format(itens[jogador]))
        print('Eu Escolhi {}'.format(itens[computador]))
        print('VOCÊ VENCEU')
    elif jogador == 2:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!')
        print('Você escolheu {}'.format(itens[jogador]))
        print('Eu Escolhi {}'.format(itens[computador]))
        print('EU GANHEI')    
elif computador == 1:
    if jogador == 0:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!')
        print('Você escolheu {}'.format(itens[jogador]))
        print('Eu Escolhi {}'.format(itens[computador]))
        print('EU GANHEI')
    elif jogador == 1:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!')
        print('Você escolheu {}'.format(itens[jogador]))
        print('Eu Escolhi {}'.format(itens[computador]))
        print('DEU EMPATE')
    elif jogador == 2:
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!')
        print('Você escolheu {}'.format(itens[jogador]))
        print('Eu Escolhi {}'.format(itens[computador]))
        print('VOCÊ VENCEU')
if jogador != 0 and jogador != 1 and jogador != 2:
    print('Jogada invalida')   
