temp = float(input('temperatura atual em °C:'))
fah = (temp * 9/5) + 32
kel = temp + 273.15
print('a temperatura atual de {:.2f}°C corresponde a'.format(temp))
print('{:.2f}°F'.format(fah))
print('{:.2f}K'.format(kel))