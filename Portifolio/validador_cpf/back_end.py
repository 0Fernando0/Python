#função para validar o cpf(string) informado 
def validar_cpf(cpf):

    numero_cpf = cpf[:-2] #cpf sem os 2 ultimos números

    soma = soma_2 = 0 #variavel  para somar os numeros do laço

    #laço para verificar numeros de numeros_cpf
    for p,numero in enumerate(range(10,1,-1)): #laço range com enumerate que começa no 10 e vai reduzindo 1 ate chegar no 2

        soma += int(numero_cpf[p])*numero #variavel soma que pega o inteiro(do numero_cpf[na posição 0,1,2...]) vezes o numero(10,9,8...)

    res_1 = 11 - (soma % 11) #variavel que realiza o calculo de validação

    numero_cpf += str(res_1) #agora adicionei em forma de string o calculo acima no numero_cpf
    
    for c,valor in enumerate(range(11,1,-1)):  #outro laço, faz a mesma coisa que o laço acima com a alteração que começa no 11

        soma_2 += int(numero_cpf[c]) * valor #faz a mesmo que a outra variavel soma

    res_2 = 11 - (soma_2 % 11) # tambem realiza o mesmo calculo que o res_1

    numero_cpf += str(res_2) # novamente adicionei em string o res_2 ao numero_cpf

    #verificando se o numero_cpf é igual(==) ao cpf de entranda da função
    print('CPF VALIDO') if numero_cpf == cpf else print('CPF INVALIDO')
    return
