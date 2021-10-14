num = float(input('digite a distancia em metros: '))
km = num / 1000
hm = num / 100
dam = num / 10
dm = num *10
cm = num * 100
mm = num * 1000
print('a medida de {:.1f}m corresponde a'.format(num))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))