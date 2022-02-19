'''
            VALIDADOR DE CPF
'''

from back_end import validar_cpf


while True:
    #usando o try para tratar erros de digitação
    try:
        cpf = int(input('DIGITE SEU  CPF (somente números): ').replace(' ','')) #passando o cpf informado para inteiro e fazendo substituição dos espaços vazios
    except:
        print('por favor somente números inteiros')
    else:
        #realizando a contagem para ver se possui os 11 caracteres
        meu_cpf = len(str(cpf))
        
        if meu_cpf  == 11:
            cpf = str(cpf) #passando o cpf(int) para string
            validar_cpf(cpf) #chamando o metodo validar_cpf do back_end.py
            break
        else:
            print('por favor verifique os números digitados')
            continue
