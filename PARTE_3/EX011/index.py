lista = []
lista1 = []
pessoa = 0
while True:
    lista.append(str(input('Qual o seu Nome: ').capitalize()))
    lista.append(float(input('Qual o seu Peso: (Kg)')))
    lista1.append(lista[:])
    lista.clear()
    pessoa += 1
    opção = str(input('Quer Continuar: [S/N] ')).upper()
    if 'N' in opção:
        break
    elif 'S' in opção:
        continue
    else:
        print('Comando Invalido Digite Outro Valor')
        continue
print(f'{lista1}')
