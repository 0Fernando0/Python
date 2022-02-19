'''
            VALIDADOR DE CPF
'''

from back_end import validar_cpf


while True:
    try:
        cpf = int(input('DIGITE SEU  CPF (somente números): ').replace(' ',''))
    except:
        print('por favor somente números inteiros')
    else:
        meu_cpf = len(str(cpf))
        if meu_cpf  == 11:
            cpf = str(cpf)
            validar_cpf(cpf)
            break
        else:
            print('por favor verifique os números digitados')
            continue
