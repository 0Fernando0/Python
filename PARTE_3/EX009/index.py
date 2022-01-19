lista = []
cont = cinco = 0
print('Digite 999 para encerrar')
while True:
    n = [int(input('escolha um número: '))]
    if n == [999]:
        print(f'foram digitados {cont} vezes')
        lista.sort(reverse=True)
        print(lista)
        if [5] in lista:
            print(f'o valor 5 foi digitado e está na lista')
        else:
            print(f'o valor 5 não se encontra na lista')
        break
    cont += 1
    lista.append(n)
    #lista.sort(reverse=         True) -> para ficar em decrescente
    #print(sorted(lista)) => para  [
    # ficar em crescente
    #print(lista.sort()) => tambem para crescente
