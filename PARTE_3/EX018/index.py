from random import randint
from time import sleep
from operator import itemgetter
jogo = {'1° Jogador':randint(1,6),
        '2° Jogador':randint(1,6),
        '3° Jogador':randint(1,6),
        '4° Jogador':randint(1,6)}
rank = dict()
for j,r in jogo.items():
    print(f'O {j}° tirou {r}')
    sleep(1)
rank = sorted(jogo.items(),key=itemgetter(1),reverse=True)
#print(rank)
n = 0
for j,r in rank:
    n += 1
    print(f'{n}° lugar: {j} tirou {r}')