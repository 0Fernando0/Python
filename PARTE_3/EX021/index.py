#def l():
#    print('='*40)
#l()
#print('Fernando')
#l()

#def linha(l):
#    print('='*40)
#    print(l)
#    print('='*40)
#linha('MEU NOME É FERNANDO')
#linha('JESUS É O SENHOR')
#linha('EU E MINHA CASA, SERVIREMOS AO SENHOR')

#def soma(a,b):
#    s = a + b
#    print(s)
#soma(1,2)

#def contador(*num):
#    print(num)
#contador(1,2,3,4)
#contador(1,3,2)
#contador(2,4)
def area(l,c):
    print(f'a área do seu terreno {l} x {c} = {t}m²')


l = float(input('largura: (m) '))
c = float(input('Comprimento: (m) '))
t = l * c
area(l,c) 