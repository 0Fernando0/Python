import math
angulo = float(input('digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('o angulo {} tem o seno de {:.2f}'.format(angulo,seno))
print('o angulo {} tem o cosseno de {:.2f}'.format(angulo,coss))
print('o angulo {} tem o tangente de {:.2f}'.format(angulo,tang))