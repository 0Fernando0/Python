'''
script que mostra o seno,consseno e tangente de um angulo
'''

from math import sin,cos,tan,radians

angulo = float(input('digite o angulo que você deseja: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))

print(f'o angulo {angulo} tem o seno de {seno:.2f}')
print(f'o angulo {angulo} tem o cosseno de {coss:.2f}')
print(f'o angulo {angulo} tem o tangente de {tang:.2f}')