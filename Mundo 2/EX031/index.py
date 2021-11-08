while True:
    n = int(input('Quer ver tabuada de Qual valor? '))
    if n == -1:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')