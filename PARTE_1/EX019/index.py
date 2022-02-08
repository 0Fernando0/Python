'''
script que seleciona um aluno para apresentação
'''


import random
lista = []
for c in range(4):
    lista.append(input(f'nome do {c+1}º aluno: '))

escolhido = random.choice(lista)
print(f'o aluno escolhido foi {escolhido}')