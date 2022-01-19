n = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte'
#while True:
#    numero = int(input('escolha um número entre (0 até 20): '))
#    if numero >= 0 and numero <= 20:
#        for pos,c in enumerate(n):
#            #print(f'{c} numero {pos}')
# #           if numero == pos:
#                print(f'você digitou {c}')
#                break
#    else:
#        print('[ERRO]')
#        reversed
while True:
    numero = int(input('escolha um número entre (0 até 20): '))
    if numero >= 0 and numero <= 20:
        for c in range(0,len(n)):
            #print(f'{c} numero {n[c]}')
            if numero == c:
                print(f'você digitou {n[c]}')
                break
    else:
        print('[ERRO]')
        reversed