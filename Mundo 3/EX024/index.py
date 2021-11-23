def maior(*n):
    print(*n)
    if len(n) == 0:
        print('não existe valor maior')
    else:
        print(f'valores {n} o maior é {max(n)}')
maior(0)