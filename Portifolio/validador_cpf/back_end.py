def validar_cpf(cpf):
    numero_cpf = cpf[:-2]
    soma = soma_2 = 0

    for p,numero in enumerate(range(10,1,-1)):
        soma += int(numero_cpf[p])*numero
    res_1 = 11 - (soma % 11)

    numero_cpf += str(res_1)
    
    for c,valor in enumerate(range(11,1,-1)):
        soma_2 += int(numero_cpf[c]) * valor
    res_2 = 11 - (soma_2 % 11)

    numero_cpf += str(res_2)

    print('CPF VALIDO') if numero_cpf == cpf else print('CPF INVALIDO')
    return
