'''
script para calcular a quantidade de tinta necessaria para pintar uma parede
'''

largura = float(input('Largura Da Parede: '))
altura = float(input('Altura Da Parede: '))
area = largura * altura 
tinta = area / 2
print(f'a parede tem dimensão de {largura} x {altura} e sua área de {area}m²')
print(f'para pintar essa parede você vai precisar de {tinta}L de tinta')