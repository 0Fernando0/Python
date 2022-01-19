larg = float(input('Largura Da Parede: '))
alt = float(input('Altura Da Parede: '))
area = larg * alt 
tinta = area / 2
print('a parede tem dimensão de {} x {} e sua área de {}m²'.format(larg,alt,area))
print('para pintar essa parede você vai precisar de {}l de tinta'.format(tinta))