times = 'atlético-MG','flamengo','palmeiras','bragantino','fortaleza','corinthians','internacional','fluminense','cuiabá','america-MG','atletico-GO','são paulo','ceara SC','athletico-PR','santos','bahia','sport recife','juventude','gremio','chapecoense'
print('OS 5 PRIMEIROS COLOCADOS')
while True:
    #print(times[:5])
    #print(times[-4:])
    #print(sorted(times))
    print('='*40)
    cont = 0
    for pos,c in enumerate(times):
        #print(f'c = {c} e pos = {pos}')
        if pos <= 4:
            print(f'{pos + 1}° COLOCADO {c}')
    print('='*20,'OS 4 ULTIMOS COLOCADOS','='*20)
    for pos,c in enumerate(times):
        if pos >= 16:
            print(f'{pos + 1}° COLOCADO {c}')
    print('='*20,'TIMES POR ORDEM ALFABETICA','='*20,)
    print(f'\n{sorted(times)}')
    print('='*50)
    for pos,c in enumerate(times):
        if c == 'chapecoense':
            print(f'ATUALMENTE A CHAPECOENSE SE ENCONTRA NA {pos + 1}° POSIÇÃO')
            print('='*50)
    break