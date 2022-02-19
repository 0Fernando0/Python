'''
script que faz a conversão de metros para as demais distancias
'''

distancia = float(input('digite a distancia em metros: '))

km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print(f'a medida de {distancia:.1f}m corresponde a')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')