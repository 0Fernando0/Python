'''
script que seleciona a ordem de apresentação dos alunos
'''

import random

lista = []
for c in range(4):
    lista.append(input(f'nome do {c+1}º aluno: '))

random.shuffle(lista)
print(f'a ordem de apresentação será \n{lista}')