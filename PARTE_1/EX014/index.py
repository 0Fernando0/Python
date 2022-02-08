'''
codigo para conversão de temperaturas de °C
para °F e K
'''

temp = float(input('temperatura atual em °C:'))

fah = (temp * 9/5) + 32

kel = temp + 273.15

print(f'a temperatura atual de {temp:.2f}°C corresponde a')
print(f'{fah:.2f}°F')
print(f'{kel:.2f}K')